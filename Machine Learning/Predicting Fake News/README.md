
# ML Project: Detecting Fake News
To utilize machine learning to distinguish between fake/unreliable and real/reliable news. 

Users are able to input their news content directly into the webpage, allowing the model to determine the validity of the given news. 
 


## Project Showcase
Webpage:

![Screenshot 2024-04-14 150542](https://github.com/dsrrenCodes/Projects/assets/120300295/ddad4c8f-05d5-4d49-b165-79a3f5a43a28)





Fake news example:



![fake example](https://github.com/dsrrenCodes/Projects/assets/120300295/00078def-81e2-4266-9299-c94c4f788ba7)




Real news example:






![image](https://github.com/dsrrenCodes/Projects/assets/120300295/f1641690-e6d6-4f5e-9b1a-f6602f5d1f1b)





## Description
Since there are only 2 possible outcomes (fake/real) news, this is a typical case of Binary Classification. Hence, logistic regression is a suitable choice to build the model. 

As we delve into text data, I opt to utilize TF-IDF (term frequency-inverse document frequency) during our preprocessing stage. TF-IDF serves as a numerical gauge to assess the relevance of words within our document collection, aiding in information retrieval and text mining endeavors. This metric inversely weighs word occurrences; thus, frequent words carry lesser significance.

Moreover, I choose to implement stemming and Stop Words elimination in our text data preprocessing.  Stemming is a method aimed at reducing inflected words to their base stems.

Using the accuracy score metric: This model is  accurate in detecting fake news.


## File guide
body_analysis.ipynb
- Using only news body content to train the model
- This varient will be used for the web apped

  
title_author_analysis.ipynb
- Using title + author name both to train the model


 webapp.py
- For deployment of the model and implementing it to a interactive webpage


body.txt 
- Test case for my model


title.txt
- Test case for my model



fakenews1.webp
- Picture for my webpage

## Dependancies
- streamlit
- nltk
- sklearn 
- Pandas
- Numpy
- Matplot
- Seaborn
## Usage
Obtain dataset from https://www.kaggle.com/c/fake-news/data?select=train.csv

Run the webapp.py file.

In command prompt, run streamlit run "(filepath)"
## Acknowledgements

 Dataset: https://www.kaggle.com/c/fake-news/data?select=train.csv
