# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:36:37 2022

@author: karaci
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,100,1) 
x_sol=[]
x_sag=[]
b_genislik=40
c_orta_nokta=50

def omuz_ciz_sol(a,b,c):
    for i,u in enumerate(x):
        if (u<=c):
            if (u<a):z.insert(i,0)
            if (u>=a and u<=b):z.insert(i,2*(pow(((u-a)/(c-a)),2)))
            if (u>b and u<=c): z.insert(i,1-2*(pow(((u-c)/(c-a)),2)))
            if (u>c): z.insert(i,1)
            x_sag.append(u)
            

def omuz_ciz_sag(a,b,c):
    for i,u in enumerate(x):
        if (u>=a):
            if (u<a):z.insert(i,1)
            if (u>=a and u<=b):z.insert(i,1-(2*(pow(((u-a)/(c-a)),2))))
            if (u>b and u<=c): z.insert(i,1-(1-2*(pow(((u-c)/(c-a)),2))))
            if (u>c): z.insert(i,0)
            x_sol.append(u)


z=[]
a=c_orta_nokta-b_genislik
b=c_orta_nokta-b_genislik/2
c=c_orta_nokta
omuz_ciz_sol(a,b,c)
plt.plot(x_sag,z)

z=[]
a=c_orta_nokta
b=c_orta_nokta+b_genislik/2
c=c_orta_nokta+b_genislik
omuz_ciz_sag(a,b,c)

plt.plot(x_sol,z)
    
    
 



