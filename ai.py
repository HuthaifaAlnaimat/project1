import pandas as pd
from keras import Sequential
from keras.layers import InputLayer, Dense
import tensorflow
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv('diabetes.csv')
train_df,test_df=train_test_split(df,test_size=0.20)

train_df=pd.DataFrame(test_df)
train_x=train_df.drop(columns=["Dutcome"],axis=1)
train_x=train_df['Dutcome']
# build the model
model=Sequential()
model.add(InputLayer(input_shape=(12,1)))
model.add(Dense(4,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
