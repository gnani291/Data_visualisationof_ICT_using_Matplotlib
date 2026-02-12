import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

font1={'family':'serif','color':'black'}
font2={'family':'serif','color':'blue','size':10}

plt.suptitle("INDIAN CRICKET TEAM",fontdict=font1,fontsize=20)

plt.subplot(2, 3, 1)
plt.title("virat kohli",fontdict=font2)
plt.plot(x,'o-k',ms=10,mec='m',mfc='y',lw=2)
plt.plot(y,'*:g',ms=10,mec='b',mfc='c',lw=2)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.title("dhoni",fontdict=font2)
plt.plot(x,'o-k',ms=10,mec='m',mfc='y',lw=2)
plt.plot(y,'*:g',ms=10,mec='b',mfc='c',lw=2)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.title("rohith",fontdict=font2)
plt.plot(x,'o-k',ms=10,mec='m',mfc='y',lw=2)
plt.plot(y,'*:g',ms=10,mec='b',mfc='c',lw=2)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.title("kl rahul",fontdict=font2)
plt.plot(x,'o-k',ms=10,mec='m',mfc='y',lw=2)
plt.plot(y,'*:g',ms=10,mec='b',mfc='c',lw=2)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.title("gill",fontdict=font2)
plt.plot(x,'o-k',ms=10,mec='m',mfc='y',lw=2)
plt.plot(y,'*:g',ms=10,mec='b',mfc='c',lw=2)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.title("pant",fontdict=font2)
plt.plot(x,'o-k',ms=10,mec='m',mfc='y',lw=2)
plt.plot(y,'*:g',ms=10,mec='b',mfc='c',lw=2)

plt.show()