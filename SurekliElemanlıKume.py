# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 09:39:21 2022

@author: karaci
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,10,0.1) 
y=np.array([])
z=[]


for i,tutx in enumerate(x):
    z.insert(i,(1/(1+pow(tutx-30/5,4))))
    y=np.append(y,(1/(1+pow(tutx-30/5,4))))
    
plt.plot(x,z)

cevap='e'
while(cevap=='e' or cevap=='E'):
    userx=float(input("1-10 arası değer girin:"))
    mx=(1/(1+pow(userx-30/5,4)))
    print("Üyelik Derecesi:",mx)
    cevap=input("Devam edecek misiniz (E/e)?")