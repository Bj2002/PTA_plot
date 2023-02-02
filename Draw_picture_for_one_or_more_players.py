from easygui import *
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'FangSong'

f = open("id2name.txt")
s = f.readline ()

choices = []
id2name = {}
n = 0

while s :
    
    l = len(s)

    id = s[0:10]
    name = s[11:l-1]

    n = n + 1

    id2name[id] = name
    choices.append(name)
    
    s = f.readline()
f.close()

lab = []
def cb(v):

    vis = {}
    for i in v.choices:
        vis[i] = 1
        print(i)

    
    
    f = open ("data.txt")


    s = f.readline()

    while (s) :

        id = s[0:10]

        name = id2name.get(id)
        if (vis.get(name)):


            y = s[11:len(s)-1].split()
            for i in range(0,len(y)) :
                y[i] = int(y[i])
            plt.plot(x, y)
            lab.append(name)
        s = f.readline()
    f.close()
    v.stop()

x = []
dcnt = 127
for i in range(dcnt) :
    x.append(i + 1)


plt.cla
multchoicebox("选择一项或多项",choices=choices,callback=cb)
plt.legend(labels=lab)
plt.show()
