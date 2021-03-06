import math
import numpy as np
import pandas as pd
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
# %matplotlib inline

com = 6758  #ソニーの株価データを取得

df = web.DataReader([str(com) + '.JP'], 'stooq').iloc[::-1]
df = df['Close']
columns = df.columns.values
index = df.index.values
scaler = MinMaxScaler().fit(df)
df = pd.DataFrame(scaler.transform(df), columns=columns, index=index)

date = df.index
price = df.iloc[:,0]
dataset = df.iloc[:,0].values

train_data = dataset[:len(dataset)//5*4]
test_data = dataset[len(dataset)//5*4:]


x_train = []
y_train = []
x_test = []
y_test = []

for i in range(len(train_data)-60):
  x_train.append(train_data[i:60+i])
  y_train.append(train_data[60+i])

for i in range(len(test_data)-60):
  x_test.append(test_data[i:60+i])
  y_test.append(test_data[60+i])

x_train, y_train, x_test, y_test = np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)
x_train, x_test = x_train.reshape(x_train.shape[0], x_train.shape[1], 1), x_test.reshape(x_test.shape[0], x_test.shape[1], 1)


model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(120))
model.add(Dense(1))
model.compile(
    optimizer='adam',
    loss='mean_squared_error')

model.fit(x_train, y_train, batch_size=1, epochs=1)

prediction = model.predict(x_test)
test = dataset[-x_test.shape[0]:]

plt.figure(figsize=(16,8))
plt.xlabel('date', color='black', size=30)
plt.ylabel('price', color='black', size=30)
plt.plot(test, label='valid')
plt.plot(prediction, label='prediction')
plt.legend()
