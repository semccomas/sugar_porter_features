import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
cmap = cm.get_cmap("RdYlBu_r",11)
plt.close('all')

def read_xvg(infile):
    with open(infile,"r") as file:
        f=file.readlines()
    X,Y,Z=[],[],[]
    for line in f:
        if line[0] not in ["@","#"]:
            X.append(float(line.split()[0]))
            Y.append(float(line.split()[1]))
            Z.append(float(line.split()[2]))
    xshape = len(np.unique(np.asarray(X)))
    yshape = len(np.unique(np.asarray(Y)))
    Z=np.asarray(Z)
    Z=np.reshape(Z,(xshape,yshape))
    Z[Z>100]=np.nan
    return Z

walker1 = "../pullx.xvg"
walker2 = "../../walker4x3_2/pullx.xvg"
walker3 = "../../walker6x3_2/pullx.xvg"
walker4 = "../../walker8x3_2/pullx.xvg"
walker5 = "../../walker10x3_2/pullx.xvg"
walker6 = "../../walker12x3_2/pullx.xvg"

a = np.loadtxt(open(walker1,'rt').readlines(), comments=["@","#",'&'], skiprows=1, usecols=(0,-1,-2), dtype=None)[::10000]
print (a.shape)
b = np.loadtxt(open(walker2,'rt').readlines(), comments=["@","#",'&'], skiprows=1, usecols=(0,-1,-2), dtype=None)[::10000]
print (b.shape)

c = np.loadtxt(open(walker3,'rt').readlines(), comments=["@","#",'&'], skiprows=-1, usecols=(0,-1,-2), dtype=None)[::10000]
print (c.shape)
d = np.loadtxt(open(walker4,'rt').readlines(), comments=["@","#",'&'], skiprows=1, usecols=(0,-1,-2), dtype=None)[::10000]
print (b.shape)
e = np.loadtxt(open(walker5,'rt').readlines(), comments=["@","#",'&'], skiprows=1, usecols=(0,-1,-2), dtype=None)[::10000]
print (b.shape)
f = np.loadtxt(open(walker6,'rt').readlines(), comments=["@","#",'&'], skiprows=1, usecols=(0,-1,-2), dtype=None)[::10000]
print (b.shape)


for i in range(1,165):

        print (i)

        plt.figure()
        j = i*1000
        infile="awh_t%s.xvg" %j
        filename = 'PMFt%s+w.png' %j

        plt.imshow(np.rot90(read_xvg(infile)),extent=(0.4, 1.2, 0.6, 1.2),cmap=cmap)
        plt.colorbar()
        #plt.legend(loc='lower right')
        plt.scatter(a[i,1],a[i,2], color='navy', label='w1')
        plt.scatter(b[i,1],b[i,2], color='darkorange', label='w2')
        #plt.scatter(c[i,1],c[i,2], color='teal', label='w3')
        plt.scatter(d[i,1],d[i,2], color='firebrick', label='w4')
        plt.scatter(e[i,1],e[i,2], color='purple', label='w5')
        plt.scatter(f[i,1],f[i,2], color='gray', label='w6')
        plt.text(1.1,1.1,str(i)+' ns')
        plt.legend(loc='lower right')

        plt.savefig(filename)
        plt.close('all')

plt.close('all')

