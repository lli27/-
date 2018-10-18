# coding=utf-8
import numpy as np
from load_data import load_data
import caffe
(X_train,Y_train)=load_data()
X_train = np.require(X_train,requirements='C')
Y_train = np.require(Y_train,requirements='C')
#m0=np.mean(X_train[:,0,:,:])
#m1=np.mean(X_train[:,1,:,:])
#m2=np.mean(X_train[:,2,:,:])
#print(np.shape(X_train))#(1000L, 3L, 224L, 224L)
#print(np.shape(Y_train))#(1000L, 2L)
#print(m0)
#print(m1)
#print(m2)
solver = caffe.SGDSolver('solver_mid_cid_clf.prototxt')
solver.net.copy_from('bvlc_alexnet.caffemodel')
solver.net.set_input_arrays(X_train, Y_train)
solver.test_nets[0].set_input_arrays(X_train, Y_train)

for i in range(2):
    solver.step(1)
#solver.step(40)#average_loss=40
#solver.net.save(r'D:\xinjian\test')


