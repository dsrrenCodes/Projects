
# ML Project: Predicting Energy Consumption 

 Time series prediction on multivariate time series using Pytorch and sklearn. Original data was univariate.
 
 I found simple models to work best than the complex models (maybe given the data preprocessing steps that favour these simple models and the obvious seasonability and trend of the original data)

 The models can be found below

 Original Dataset Distribution: 
 
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

## LSTM Results

## GRU Results

## Ridge Regression Results

## Random Forest Regressor Results