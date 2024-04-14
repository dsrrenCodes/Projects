from PIL import Image
import streamlit as st


import pandas as pd
import numpy as np
import re

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#Stemmers remove morphological affixes from words, leaving only the word stem.
from nltk.stem.porter import PorterStemmer

#convert text into feature vectors (numerical data)
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

#model
from sklearn.linear_model import LogisticRegression

#metrics
from sklearn.metrics  import accuracy_score
dslist=stopwords.words('english')




def predict_news(news_text):
    
    #Preprocess the news text
    processed_text = stemmingprocess(news_text)

    #Vectorize the text using the loaded TfidfVectorizer
    vectorized_text = vector.transform([processed_text])

    #Predict using the loaded LogisticRegression model
    prediction = classifier.predict(vectorized_text)[0]

    return "Real" if prediction == 0 else "Fake"








def stemmingprocess(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content=stemmed_content.lower()
    stemmed_content=stemmed_content.split()
    singles=[stemmer.stem(x) for x in stemmed_content if not x in dslist]
    stemmed_content=" ".join(singles)

    return stemmed_content



def predict_fake_news(news_text):
    # Your ML model prediction logic here
    # Replace this placeholder logic with your actual ML model prediction
    return predict_news(news_text)



def main():
    image=Image.open('C:/Users/Darren/Desktop/Fake_news/fakenews1.webp')
    st.image(image,caption='ML to detect fake news',use_column_width=True)
    st.title("Fake News Detection with Logistic Regression!")
    st.write("Detect if news content provided is fake/unreliable or real/reliable using my Machine Learning Model!")
 
    st.write("Enter the news text below:")
    # User input text box
    user_input = st.text_area("")


    
    


    if st.button("Detect"):
        # Call the prediction function
        prediction = predict_fake_news(user_input)
        st.write("The news is:", prediction)


if __name__ == "__main__":
    stemmer=PorterStemmer()
    vector=TfidfVectorizer()
    classifier=LogisticRegression()
    newsdf=pd.read_csv('C:/Users/Darren/Desktop/Fake_news/train.csv')
    newsdf=newsdf.fillna(" ")
    newsdf=newsdf.drop(columns=['author'])
    newsdf['content']=newsdf['title']+newsdf['text']
    
    newsdf['content']=newsdf['content'].apply(stemmingprocess)
    
    numText = vector.fit_transform(newsdf['content'])
    X=numText
    Y=newsdf['label']
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.9,test_size=0.1,stratify=Y,random_state=2)
    
    classifier.fit(X_train,Y_train)
    main()




#run app in command line
# streamlit run webapp.py
#