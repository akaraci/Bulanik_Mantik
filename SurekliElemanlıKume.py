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
    
    
#Döngü kullanılmadan aşağıdaki satır da aynı fonskiyonu hesaplar.
#c=np.append(y,(1/(1+pow(x-30/5,4))))  

plt.plot(x,z)

