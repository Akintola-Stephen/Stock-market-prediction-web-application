import numpy as np
import pandas as pd
import joblib

import warnings
warnings.filterwarnings('ignore')

csv_path = 'stock-market-prediction-web-application/stock_prediction/ML/code/dataset/all_stocks_5yr.csv'
df = pd.read_csv(csv_path)

print(df.shape)

df['open'] = df['open'].fillna(df['open'].mean())
df['high'] = df['high'].fillna(df['high'].mean())
df['low'] = df['low'].fillna(df['low'].mean())

print(df.isna().sum() / len(df))

drop_cols = ['date', 'Name']
df.drop(drop_cols ,axis = 1, inplace = True)

cols = ['open', 'high', 'low', 'close']
X = df[cols]
y = df['volume']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

print(
    'X_train shape and X_test are {0} {1} respectively' 
    'while y_train and y_test shape are {2} {3}'.format(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    )

from sklearn.linear_model import ARDRegression
ar = ARDRegression()

ar.fit(X_train, y_train)
print(ar.score(X_train, y_train))

prediction = ar.predict(X_train)

joblib.dump(ar, 'model.pkl')

