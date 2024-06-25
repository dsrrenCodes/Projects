import streamlit as st
import pickle
import fitz  # PyMuPDF for PDF handling
import io
import re

def cleanResume(txt):
    #removing links
    cleanText = re.sub('http\S+\s', ' ', txt)
    #removing keywords
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)  
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText) 
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText

# Initialize session state
if 'loaded_model' not in st.session_state:
    st.session_state.loaded_model = None

if 'loaded_vector' not in st.session_state:
    st.session_state.loaded_vector = None

# Load your pre-trained model and vectorizer if not already loaded
if st.session_state.loaded_model is None or st.session_state.loaded_vector is None:
    try:
        with open('models/randomforest_model.pkl', 'rb') as model_file:
            st.session_state.loaded_model = pickle.load(model_file)

        with open('models/vector.pkl', 'rb') as vector_file:
            st.session_state.loaded_vector = pickle.load(vector_file)
    except Exception as e:
        st.error(f"Error loading model or vectorizer: {e}")

# Title and header
st.title("Resume Classifier")
st.write('Conducted Random Search Cross Validation on Random Forest Model with 88% accuracy using data from https://www.kaggle.com/datasets/noorsaeed/resume-datasets')
st.write('Simply upload your PDF file and see what the model classifies what sector/job your resume belongs too')
# Centered image or logo (adjust width as needed)
st.image("ai_resume.png", width=800)

# File uploader for PDF
st.header("Upload a PDF file")
pdf_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if pdf_file is not None:
    try:
        # Display details of the uploaded file
        file_details = {"FileName": pdf_file.name, "FileType": pdf_file.type}
        st.write(file_details)

        # Button to convert and display text
        if st.button("Convert and Display Text"):
            # Ensure file is uploaded and ready
            if hasattr(pdf_file, 'read'):
                # Use io.BytesIO to handle the uploaded file
                pdf_data = io.BytesIO(pdf_file.read())
                
                # Read the PDF file using fitz.open
                pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
                
                # Extract text from each page
                pdf_text = ""
                for page_num in range(len(pdf_document)):
                    page = pdf_document.load_page(page_num)
                    pdf_text += page.get_text()
                pdf_text=cleanResume(pdf_text)
                
                # Display extracted text
                st.subheader("Extracted Text from PDF")
                st.write(pdf_text)
                
                # Close the PDF document
                pdf_document.close()
                
                # Button to predict classification
                
                    # Ensure vectorizer and model are loaded and compatible
                if st.session_state.loaded_vector and st.session_state.loaded_model:
                        # Transform text using loaded vectorizer
                        input_vector = st.session_state.loaded_vector.transform([pdf_text])
                        
                        # Predict using loaded model
                        prediction = st.session_state.loaded_model.predict(input_vector)
                        
                        # Display prediction result
                        
                        st.write(f"Model Prediction: **{prediction[0]}**")

                        
                else:
                        st.warning("Model or vectorizer not loaded properly.")
                
            else:
                st.warning("Please upload a PDF file.")
            
            
        
    except Exception as e:
        st.error(f"Error processing PDF: {e}")