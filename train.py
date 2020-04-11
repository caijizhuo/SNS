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
#     ipbit = list(map(int,row[0].split('.')))
    tp = row[1].strip()
    tp = float(tp)
    tp = int(tp)
    X.append(ipbit)
    y.append(tp)

X = np.array(X)
y = np.array(y)


# tensorboard = TensorBoard(log_dir='.\logs')

X_train,y_train = X[:7200],y[:7200]
X_test,y_test = X[8000:],y[8000:]

X_val = X[7200:8000]
y_val = y[7200:8000]

#-----params---------
layernum = [1,2,3,4,5]
actfunc = ['relu','sigmoid']
nodenum = [16,32,64,128]

for ln in layernum:
    for n in nodenum:
        for f in actfunc:
            model = Sequential()
            model.add(Dense(output_dim = n,input_dim=32,activation=f))
            for l in range(ln):
                model.add(Dense(output_dim = n,activation=f))
            model.add(Dense(output_dim = 1))
            model.compile(optimizer='adam', loss='mse')
            epochs = 100
            
            print('--------Training-------')
            # for i in range(epochs):
            his = model.fit(X_train,y_train,batch_size=32,shuffle=False,epochs = epochs,validation_data=(X_val,y_val))
            modelname = 'layer'+str(ln)+'_'+'node'+str(n)+'_'+'acf'+str(f)+'.h5'
            modelpath = 'models/' + modelname
            model.save(modelpath)
            with open('param.txt','a+') as f:
                f.write(modelname)
                f.write('#')
                for i in his.history['val_loss']:
                    f.write(str(i))
                    f.write(',')
                f.write('#')
                for i in his.history['loss']:
                    f.write(str(i))
                    f.write(',')
                f.write('\n')


# print('---------TEST----------')
# res = model.evaluate(X_test,y_test,batch_size=32)
# print(res)