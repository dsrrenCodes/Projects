
# ML Project: Predicting Energy Consumption 

 Time series prediction on multivariate time series using Pytorch and sklearn. Original data was univariate.
 
 I found simple models to work best than the complex models (maybe given the data preprocessing steps that favour these simple models and the obvious seasonability and trend of the original data)

 The models can be found below

 Original Dataset Distribution: 
 ![image](https://github.com/user-attachments/assets/e55b927c-0745-427e-9798-fb5e270da343)

## Workflow

1. EDA
- Analyzed the dataset to check for missing values and whether data is in chronological order and have equidistant timestamps

2. Data preprocessing
- Generated time lags
- Performed feature engineering on data column to get more features
- One hot encode features
- Generated Cylical features from selected columns
- Added Holidays column
- Split data into train,validation,test set and scaled them accordingly as well as convert them into tensors for pytorch models
- Added sequence length to data to be eligible for the pytorch models 

3. Model Development:
- Developed RNN,LSTM, GRU models using PyTorch
- Developed baseline Ridge Regression and Random Forest Regression models from sklearn
- Created a class function that integrates training,evaulation and the plotting of loss curves for PyTorch models
- Created helper functions that deal with formating the model's prediction including its performance metrics and its prediction to actual results plot.

## Model Performances
## RNN Results
![rnn result1](https://github.com/user-attachments/assets/b79a828a-48e1-4e1d-97b7-df7ba8e757f3)


## LSTM Results
![lstm result](https://github.com/user-attachments/assets/d876ae3d-c89f-4242-ae31-c26c7c2247cc)

## GRU Results
![gru result](https://github.com/user-attachments/assets/60268590-ed97-49bf-9a74-64290bacc2e2)

## Ridge Regression Results
![Ridge Regression Result](https://github.com/user-attachments/assets/1c3417b4-4065-4b27-bc59-a95de2f975b6)

## Random Forest Regressor Results
![Random Forest regressor result](https://github.com/user-attachments/assets/c4689da3-0f3c-43d0-ae96-1f563f75b7c9)

