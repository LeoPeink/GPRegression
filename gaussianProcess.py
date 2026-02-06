#open CSV as pandas dataframe
import pandas as pd
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor #TODO remove
from sklearn.gaussian_process.kernels import RBF, WhiteKernel #TODO remove
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

df = load_data("PROJECT/Italy.csv")
#EXPLORATORY ANALYSIS
print(df.head())
print(df.info())
print(df.describe())


#PREPROCESSING
#check for missing values
print("Missing values in each column:")
print(df.isnull().sum())
#handle missing values if any (e.g., drop or impute)
df = df.dropna()
#convert date column to datetime