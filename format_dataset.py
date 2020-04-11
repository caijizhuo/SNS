with open('iptp.txt','r') as f:
    row = f.readlines()
for i in range(len(row)):
    t = row[i].split(',')
    row[i] = t

ipres = []
for i in row:
    if i[0]=='-1':
        continue
    x = i[0].split('.')
    ipbit = ''
    for j in x:
        ipbit += format(int(j),'08b')
    ipbit = ipbit + ','
    tp = int(float(i[1].strip())/1024)
    ipbit = ipbit + str(tp) + '\n'
    ipres.append(ipbit)

with open('dataset.csv','w') as f:
    for i in ipres:
        f.write(i)
