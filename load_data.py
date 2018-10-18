# coding=utf-8
import os
from PIL import Image
import numpy as np
import xlrd

def load_data():
    #Return a new array of given shape and type, without initializing entries.
	data = np.empty((1000,3,227,227),dtype=np.float32)
	label = np.empty((1000,2),dtype=np.float32)
    #os.listdir(filename)返回filename中所有文件的文件名列表
	imgs = os.listdir(r'D:/lily/test1')
	num = len(imgs)
	xls=xlrd.open_workbook(r'D:\lily\Book.xlsx')
	sheet=xls.sheet_by_name('Sheet1')
	for i in range(num):
		#PIL 的 open() 函数用于创建 PIL 图像对象
		img = Image.open(r'D:/lily/test1/'+imgs[i])
        #Convert the input to an array
		arr = np.asarray(img,dtype=np.float32)
		arr = arr.reshape((3,227,227))
		data[i,:,:,:] = arr
		label[i][0]=sheet.cell_value(i+1,3)#model id
		label[i][1]=sheet.cell_value(i+1,4)#vehicle id
	m0=np.mean(data[:,0,:,:])
	m1=np.mean(data[:,1,:,:])
	m2=np.mean(data[:,2,:,:])
	data[:,0,:,:]=data[:,0,:,:]-np.asarray(np.ones((1000,227,227))*m0,dtype=np.float32)
	data[:,1,:,:]=data[:,1,:,:]-np.asarray(np.ones((1000,227,227))*m1,dtype=np.float32)
	data[:,2,:,:]=data[:,2,:,:]-np.asarray(np.ones((1000,227,227))*m2,dtype=np.float32)
	return data,label
