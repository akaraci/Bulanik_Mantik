# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:28:13 2022

@author: karaci
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#-----------Değişkenler ve Evrensel kümeler tanımlanıyor
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')
#-------------------------------------------------------

#---------Bulanık Kümeler Tanımlanıyor ve grafik olarak gösteriliyor----------------
# Auto-membership function population is possible with .automf(3, 5, or 7)
#Otomatik üyelik fonksiyonları oluşturuluyor. İtsenirse 5 ya da 7 küme de olutşrulabilir
quality.automf(3)
service.automf(3)
#Bahşiş için üyelik fonksiyonları manuel oluşturuluyor
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

#--bulanık küme grafikleri çizdiriliyor
quality.view()
service.view()
tip.view()
#quality['average'].view() #tüm kümeler gösterilir ancak average kümesi kalın çizgiyle gösterilir.
#---------------------------------------------------------

#----------------------Kurallar oluşturuluyor----------------------
# If the food is poor OR the service is poor, then the tip will be low
# If the service is average, then the tip will be medium
# If the food is good OR the service is good, then the tip will be high.
rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])
#-----------------------------------------------------------------------

#-----Kontrol sistemi oluşturuluyor
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
#In order to simulate this control system, we will create a ControlSystemSimulation
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# Girişlere karşı çıkışlar hesaplanıyor
tipping.compute()
print ("",tipping.output['tip'])
tip.view(sim=tipping)






