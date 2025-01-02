
# ML Project: Sentimental Analysis using IMDB Dataset (movie reviews)

 Performing binary sentiment classification (positive/negative) of users' reviews. 
 
## Workflow

1. EDA
- Analyzed the dataset to identify and remove redundant information, such as URLs, HTML tags, and non-alphanumeric characters.

2. Data preprocessing
- Cleaned the text by removing redundant elements using regex
- Eliminated stop words and applied lemmatization to standardize word forms using NLTK  
- Corrected spelling errors using the SymSpellPy library for enhanced text consistency
- Tokenized words according to their frequency
- Utilized padding , where each review is padded with 0's or truncated to the input seq_length.

3. Model Development:
- Developed a simple LSTM model using PyTorch
- Optimized the model by leveraging Optuna for hyperparameter tuning (embedding dim, number of hidden units, LSTM layers, and dropout rates).
- Employed cross-validation to identify the optimal combination of hyperparameters, leading to improved model performance.
- Performance metric of holdout set: 0.94 ROC AUC score.

Example

![image](https://github.com/user-attachments/assets/b9c64f71-416a-4096-8f3d-a93f0401c2e0)
