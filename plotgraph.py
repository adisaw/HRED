import numpy as np 
import matplotlib.pyplot as plt
data=np.genfromtxt('result', dtype=np.float64, delimiter=',')
xval=np.zeros(data.shape[0])
yval=np.zeros(data.shape[1])
xval=data[:,0]
yval=data[:,1]

plt.plot(xval,yval,'b-',marker='.')
plt.xlabel('Number of Iterations')
plt.ylabel('Negative Log Likelihood Loss')
plt.title('NLLLoss vs No of Iterations')
#Saving plot
plt.savefig('ResultPlot.png')
plt.clf()