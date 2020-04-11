import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
from keras import optimizers
import random

with open('dataset.csv') as f:
    data = f.readlines()
X = []
y = []
# print(len(data))
random.shuffle(data)
for row in data:
    row = row.split(',')
    ipbit = list(map(int,list(row[0])))
    tp = row[1].strip()
    tp = float(tp)
    tp = int(tp)
    X.append(ipbit)
    y.append(tp)

X = np.array(X)
y = np.array(y)


X_train,y_train = X[:7200],y[:7200]
X_test,y_test = X[8000:],y[8000:]

X_val = X[7200:8000]
y_val = y[7200:8000]

# find the best model in 300 epochs ------------------------
# model = Sequential()
# model.add(Dense(output_dim = 32,input_dim=32,activation='relu'))
# model.add(Dense(output_dim = 16,activation='relu'))
# model.add(Dense(output_dim = 16,activation='relu'))
# model.add(Dense(output_dim = 16, activation='relu'))
# model.add(Dense(output_dim = 1))
# model.compile(optimizer='adam', loss='mse')


# epochs = 300
# his = model.fit(X_train,y_train,batch_size=32,shuffle=False,epochs = epochs,validation_data=(X_val,y_val))

# x = range(300)
# plt.plot(x,his.history['val_loss'],label='val_loss',c='r')
# plt.grid(linestyle='-.',linewidth=1)
# plt.xlabel("epochs")
# plt.ylabel("MSE")
# plt.legend()
# plt.show()

# the best model:60 epochs -------------------------
fmodel = Sequential()
fmodel.add(Dense(output_dim = 32,input_dim=32,activation='relu'))
fmodel.add(Dense(output_dim = 16,activation='relu'))
fmodel.add(Dense(output_dim = 16,activation='relu'))
fmodel.add(Dense(output_dim = 16, activation='relu'))
fmodel.add(Dense(output_dim = 1))
fmodel.compile(optimizer='adam', loss='mse')
his1 = fmodel.fit(X_train,y_train,batch_size=32,shuffle=False,epochs = 60,validation_data=(X_val,y_val))

# find best batchsize ------------------------
size = [8,16,32,64,128,256]
# for s in size:
# 	model = Sequential()
# 	model.add(Dense(output_dim = 32,input_dim=32,activation='relu'))
# 	model.add(Dense(output_dim = 16,activation='relu'))
# 	model.add(Dense(output_dim = 16,activation='relu'))
# 	model.add(Dense(output_dim = 16, activation='relu'))
# 	model.add(Dense(output_dim = 1))
# 	model.compile(optimizer='adam', loss='mse')

# 	his2 = model.fit(X_train,y_train,batch_size=s,shuffle=False,epochs = 100,validation_data=(X_val,y_val))
# 	with open('batchsize.txt','a+') as f:
# 		f.write('batch size:')
# 		f.write(str(s))
# 		f.write('#')
# 		for i in his2.history['val_loss']:
# 			f.write(str(i))
# 			f.write(',')
# 		f.write('\n')

# x = range(100)
# plt.plot(x,his1.history['val_loss'],label='val_loss8',c='r')
# plt.plot(x,his2.history['val_loss'],label='val_loss32',c='g')
# plt.grid(linestyle='-.',linewidth=1)
# plt.xlabel("epochs")
# plt.ylabel("MSE")
# plt.legend()
# plt.show()

# print('---------TEST----------')
res = fmodel.evaluate(X_test,y_test,batch_size=32)
print(res)