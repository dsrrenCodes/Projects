from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import openai


app = Flask(__name__)
app.secret_key = 'verysecretkey'  # Change this to a real secret key in production

# Mock database of users
users = {}


@app.route('/')
def index():
    # Redirect to home if logged in, else to login
    if 'user' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)

        if user and check_password_hash(user['password'], password):
            session['user'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users:
            flash('Username already exists.')
            return redirect(url_for('signup'))

        users[username] = {'username': username, 'password': generate_password_hash(password)}
        session['user'] = username
        return redirect(url_for('home'))

    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/index')
def classes():
    if 'user' in session:
        return render_template('index.html', user=session['user'])
    return redirect(url_for('index.html'))

@app.route('/feedback')
def feedback():
    if 'user' in session:
        return render_template('feedback.html', user=session['user'])
    return redirect(url_for('feedback.html'))





#
current_data = pd.read_csv('AY 2024 class data set.csv', dtype={'class': str})
previous_year_data = pd.read_csv('AY2023 class data set.csv', dtype={'class': str})


openai.api_key = 'sk-proj-m0PHnIPT3zaBDn8IVtwyT3BlbkFJSZMw6s7cxhg6E8AwmyHg'


def compare_scores(current_scores, previous_scores):
    score_differences = {}
    for subject, current_score in current_scores.items():
        if subject in previous_scores:
            try:
                diff = float(current_score) - float(previous_scores[subject])
                score_differences[subject] = diff
            except ValueError:
                continue
    return score_differences


def generate_insights(student_data):
    try:
        attendance_rate = float(str(student_data.get('attendance_rate', '0')).replace('%', ''))
        num_of_cca = int(student_data.get('num_of_cca', 0))
        siblings_size = int(student_data.get('sibs_size', 0))
        parents_size = int(student_data.get('p_size', 0))
        household_income = float(student_data.get('monthly_household_income', 0))


        family_size = siblings_size + parents_size + 1
        income_per_family_member = household_income / family_size if family_size != 0 else float('inf')


        student_name = student_data.get('student_name', 'Unknown')
        gender = student_data.get('gender', 'Unknown')


        criteria_met = {
            "large_family": family_size > 5,
            "low_income": income_per_family_member < 3000,
            "high_cca": num_of_cca > 1,
            "low_attendance": attendance_rate < 80
        }


        score_fields = ['a math', 'e math', 'bio', 'phy', 'chem', 'english', 'mother_tongue', 'fnn', 'geography', 'lit', 'dnt']
        current_scores = {f'score_{subject}': student_data.get(subject, '0') for subject in score_fields}
        previous_scores = {}
        prev_student_data = previous_year_data[previous_year_data['student_name'] == student_name]
        if not prev_student_data.empty:
            previous_scores = {f'score_{subject}': prev_student_data.iloc[0].get(subject, '0') for subject in score_fields}


        score_differences = compare_scores(current_scores, previous_scores)


        prompt = f"Student Name: {student_name}\nGender: {gender}\nSiblings Size: {siblings_size}\nParents Size: {parents_size}\nHousehold Income: {household_income}\nNumber of CCAs: {num_of_cca}\nAttendance Rate: {attendance_rate}\n\n"
        if criteria_met["large_family"]:
            prompt += "The student comes from a large family with more than 5 members.\n"
        if criteria_met["low_income"]:
            prompt += "The household income per family member is less than $3000.\n"
        if criteria_met["high_cca"]:
            prompt += "The student is involved in more than 1 CCA.\n"
        if criteria_met["low_attendance"]:
            prompt += "The student's attendance rate is less than 80%.\n"


        significant_decrease = False
        significant_increase = False


        for subject, diff in score_differences.items():
            if diff < -20:
                significant_decrease = True
            elif diff > 20:
                significant_increase = True


        if significant_decrease:
            prompt += "There has been a significant decrease in the student's scores compared to the previous year.\n"
        if significant_increase:
            prompt += "There has been a significant increase in the student's scores compared to the previous year.\n"


        prompt += "Given these factors, why might this student be underperforming and what actions can the teacher take?"


        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "I am an educational advisor."},
                {"role": "user", "content": prompt}
            ]
        )


        insights = response.choices[0].message['content'].strip()
        insights = insights.replace("**", "")


        return insights


    except Exception as e:
        print(f"Error generating insights: {e}")
        return "There was an error generating insights for this student."






@app.route('/student/<int:student_id>')
def student(student_id):
    student_data = current_data.iloc[student_id].to_dict()


    for key, value in student_data.items():
        if pd.isna(value) or value == '':
            student_data[key] = "0"


    insights = generate_insights(student_data)
    return render_template('indiv_dashboard.html', student=student_data, insights=insights)


@app.route('/class-list')
def dashboard():
    df = current_data
    students_df = df.head(10)


    grade_columns = ["a math", "e math", "bio", "phy", "chem", "english", "mother_tongue", "fnn", "geography", "lit", "dnt"]
    students_df[grade_columns] = students_df[grade_columns].apply(pd.to_numeric, errors='coerce')
    students_df["average_grade"] = students_df[grade_columns].mean(axis=1)


    students_df = students_df.sort_values(by='average_grade', ascending=False)
    students_df['rank'] = students_df['average_grade'].rank(ascending=False, method='dense').astype(int)


    colors = np.where(students_df['average_grade'] < 60, 'salmon', 'cornflowerblue')
    plt.figure(figsize=(12, 6))
    plt.xlabel('Name')
    plt.ylabel('Average Grade (out of 100)')
    bars = plt.bar(students_df['student_name'], students_df['average_grade'], color=colors)
    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{students_df["average_grade"].iloc[i]:.1f}', ha='center', va='bottom')
    for i, avg_grade in enumerate(students_df["average_grade"]):
        if avg_grade < 60:
            bars[i].set_color('salmon')
    legend_elements = [
        plt.Line2D([0], [0], color='salmon', lw=4, label='Struggling'),
        plt.Line2D([0], [0], color='cornflowerblue', lw=4, label='Passing'),
    ]
    plt.legend(handles=legend_elements, loc='upper right')
    plt.ylim(0, 110)
    plt.xticks(rotation=15)
    plt.tight_layout()


    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data_uri = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()


    students_df = students_df.fillna('N/A')
    students_list = students_df.to_dict(orient='records')


    return render_template('dashboard.html', students=students_list, plot_data_uri=plot_data_uri, grade_columns=grade_columns)

if __name__ == '__main__':
    app.run(debug=True)


