# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:22:13 2023

@author: akara
"""

from simpful import *
FS = FuzzySystem()

# Define fuzzy sets and linguistic variables
S_1 = FuzzySet(points=[[0., 1.],  [5., 0.]], term="poor")
S_2 = FuzzySet(points=[[0., 0.], [5., 1.], [10., 0.]], term="good")
S_3 = FuzzySet(points=[[5., 0.],  [10., 1.]], term="excellent")
FS.add_linguistic_variable("Service", LinguisticVariable([S_1, S_2, S_3], concept="Service quality"))

F_1 = FuzzySet(points=[[0., 1.],  [10., 0.]], term="rancid")
F_2 = FuzzySet(points=[[0., 0.],  [10., 1.]], term="delicious")
FS.add_linguistic_variable("Food", LinguisticVariable([F_1, F_2], concept="Food quality"))

FS.plot_variable("Service",element=6.5)
FS.plot_variable("Food",element=9.8)

# Define output crisp values
FS.set_crisp_output_value("small", 5)
FS.set_crisp_output_value("average", 15)
# Define function for generous tip (food score + service score + 5)
FS.set_output_function("generous", "Food+Service+5")

print("\n--------------------------------------------")
print("Service->poor member degree:",S_1.get_value(6.5))
print("Service->good member degree:",S_2.get_value(6.5))
print("Service->excellent member degree:",S_3.get_value(6.5))
print("\n--------------------------------------------")
print("Food->rancid member degree:",F_1.get_value(9.8))
print("Food->delicious member degree:",F_2.get_value(9.8))


# Define fuzzy rules
R1 = "IF (Service IS poor) OR (Food IS rancid) THEN (Tip IS small)"  #0.0199 üyelik derecesi gelir, k=5
R2 = "IF (Service IS good) THEN (Tip IS average)" #0.7 üyelik derecesi gelir, k=15
R3 = "IF (Service IS excellent) OR (Food IS delicious) THEN (Tip IS generous)" #0.98 üyelik derecesi gelir, k=Food+Service+5=9.8+6.5+5=21.3
FS.add_rules([R1, R2, R3])

# Set antecedents values
FS.set_variable("Service",6.5 )
FS.set_variable("Food", 9.8)

#0.0199*5+0.7*15+0.98*21.3/(0.0199+0.7+0.98)
#(0.0995+10.5+20.874)/1.699=31.4735/1.699=18.524
# Perform Sugeno inference and print output
print(FS.Sugeno_inference(["Tip"]))

