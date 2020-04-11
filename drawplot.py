import matplotlib.pyplot as plt
index = []
val_loss = []
with open('param.txt','r') as f:
    rows = f.readlines()
# with open('batchsize.txt','r') as f:
#     rows = f.readlines()

for row in rows:
    data = row.split('#')
    index.append(data[0])
    l = data[1].split(',')
    l.pop(100)
    l = list(map(float,l))
    val_loss.append(l)

# with open('batchsize.txt','r') as f:
#     rows = f.readlines()

# for row in rows:
#     data = row.split(',')
#     data.pop(100)
#     l = list(map(float,data))
#     val_loss.append(l)

x = range(100)
color = ['red','green','gold','blue','black','lime','navy','darkviolet']

for i in range(32,40):
    plt.plot(x,val_loss[i],label=index[i],c=color[i%8])
# plt.title("Relu")
plt.grid(linestyle='-.',linewidth=1)
plt.xlabel("epochs")
plt.ylabel("MSE")
plt.legend()
plt.show()