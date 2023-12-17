# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 20:52:15 2023

@author: akara
"""

from simpful import *
import matplotlib.pyplot as plt

FS = FuzzySystem()

TLV = AutoTriangle(3, terms=['poor', 'average', 'good'], universe_of_discourse=[0,10])
FS.add_linguistic_variable("service", TLV)
FS.add_linguistic_variable("quality", TLV)


O1 = TriangleFuzzySet(0,0,13,   term="low")
O2 = TriangleFuzzySet(0,13,25,  term="medium")
O3 = TriangleFuzzySet(13,25,25, term="high")
FS.add_linguistic_variable("tip", LinguisticVariable([O1, O2, O3], universe_of_discourse=[0,25]))


fig,(ax0,ax1,ax2,ax3)=plt.subplots(nrows=4,figsize=(15,20))


FS.plot_variable("service",element=9.8,ax=ax0) #element=2, verilen değerin kümelere üyeliğini gösterir.
FS.plot_variable("quality",element=6.5,ax=ax1) #element=2, verilen değerin kümelere üyeliğini gösterir.
FS.plot_variable("tip",ax=ax2)

FS.add_rules([
	"IF (quality IS poor) OR (service IS poor) THEN (tip IS low)",
	"IF (service IS average) THEN (tip IS medium)",
	"IF (quality IS good) OR (service IS good) THEN (tip IS high)"
	])

FS.set_variable("quality", 6.5) 
FS.set_variable("service", 9.8) 

tip=FS.Mamdani_inference()
print(tip)
FS.plot_variable("tip",element=tip['tip'],ax=ax3)
