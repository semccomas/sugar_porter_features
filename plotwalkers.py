??? from here until ???END lines may have been inserted/deleted
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
cmap = cm.get_cmap("RdYlBu_r",11)
plt.close('all')

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

        plt.plot(a[:,1],a[:,2], color='navy', label='w1')
        plt.plot(b[:,1],b[:,2], color='darkorange', label='w2')
        plt.plot(c[:,1],c[:,2], color='teal', label='w3')
        plt.plot(d[:,1],d[:,2], color='firebrick', label='w4')
        plt.plot(e[:,1],e[:,2], color='purple', label='w5')
        plt.plot(f[:,1],f[:,2], color='gray', label='w6')


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

???END
