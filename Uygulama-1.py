# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:39:23 2022

@author: karaci
"""
import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt


var_pedal=np.arange(0,101,1)
var_speed=np.arange(0,101,1)
var_brake=np.arange(0,101,1)

#Üçgen Üyelik Fonksiyonları Tanımlanıyor
set_pedal_low=mf.trimf(var_pedal, [0,0,50])
set_pedal_med=mf.trimf(var_pedal, [0,50,100])
set_pedal_hig=mf.trimf(var_pedal, [50,100,100])

set_speed_low=mf.trimf(var_speed, [0,0,60])
set_speed_med=mf.trimf(var_speed, [20,50,80])
set_speed_hig=mf.trimf(var_speed, [40,100,100])

set_brake_poor=mf.trimf(var_brake, [0,0,100])
set_brake_strong=mf.trimf(var_brake, [0,100,100])


fig,(ax0,ax1,ax2)=plt.subplots(nrows=3,figsize=(6,10))
ax0.plot(var_pedal,set_pedal_low,'r',linewidth=2, label='Düşük')
ax0.plot(var_pedal,set_pedal_med,'g',linewidth=2, label='Orta')
ax0.plot(var_pedal,set_pedal_hig,'b',linewidth=2, label='Yüksek')
ax0.set_title("Pedal Basıncı")
ax0.legend()


ax1.plot(var_speed,set_speed_low,'r',linewidth=2, label='Düşük')
ax1.plot(var_speed,set_speed_med,'g',linewidth=2, label='Orta')
ax1.plot(var_speed,set_speed_hig,'b',linewidth=2, label='Yüksek')
ax1.set_title("Araç Hızı")
ax1.legend()

ax2.plot(var_brake,set_brake_poor,'r',linewidth=2, label='Zayıf')
ax2.plot(var_brake,set_brake_strong,'b',linewidth=2, label='Güçlü')
ax2.set_title("Fren")
ax2.legend()


input_pedal=40
input_speed=75


#Girişlerin Üyelik fonksiyonlara üyelik dereceleri hesaplanıyor
pedal_fit_low=fuzz.interp_membership(var_pedal,set_pedal_low,input_pedal)
pedal_fit_med=fuzz.interp_membership(var_pedal,set_pedal_med,input_pedal)
pedal_fit_hig=fuzz.interp_membership(var_pedal,set_pedal_hig,input_pedal)
print("Pedal Giriş Değişkenin Üyelik Fonksiyonlarına Üyelik Deereceleri")
print("Pedal Basıncı Düşük Kümesine Üyelik Derecesi:",pedal_fit_low)
print("Pedal Basıncı Orta Kümesine Üyelik Derecesi:",pedal_fit_med)
print("Pedal Basıncı Yüksek Kümesine Üyelik Derecesi:",pedal_fit_hig)

speed_fit_low=fuzz.interp_membership(var_speed,set_speed_low,input_speed)
speed_fit_med=fuzz.interp_membership(var_speed,set_speed_med,input_speed)
speed_fit_hig=fuzz.interp_membership(var_speed,set_speed_hig,input_speed)
print("Hız Giriş Değişkenin Üyelik Fonksiyonlarına Üyelik Deereceleri")
print("Hız Düşük Kümesine Üyelik Derecesi:",speed_fit_low)
print("Hız Basıncı Orta Kümesine Üyelik Derecesi:",speed_fit_med)
print("Hız Basıncı Yüksek Kümesine Üyelik Derecesi:",speed_fit_hig)


#Kural Tabanı Oluşturuluyor
#mamdani min metodu soncul çıkış künesine uygulanıyor. Öncüllerden elde edilen üyelik derecesinden çıkış kümesi kesiliyor.
rule1 = np.fmin(pedal_fit_med, set_brake_strong)
rule2 = np.fmin(np.fmin(pedal_fit_hig, speed_fit_hig), set_brake_strong) 
rule3 = np.fmin(np.fmax(pedal_fit_low, speed_fit_low), set_brake_poor) 
rule4 = np.fmin(pedal_fit_low, set_brake_poor)


#dot-max öncüllerden elde edilen üyelik değerleri soncul çıkış kümesi üyelik dereceleriyle çarpılarak ölçekleniyor
# rule1 = pedal_fit_med*set_brake_strong
# rule2 = np.fmin(pedal_fit_hig, speed_fit_hig)*set_brake_strong
# rule3 = np.fmax(pedal_fit_low, speed_fit_low)*set_brake_poor
# rule4 = pedal_fit_low*set_brake_poor


out_strong=np.fmax(rule1,rule2)
out_poor=np.fmax(rule3,rule4)



brake0 = np.zeros_like(var_brake)
fig, ax0 = plt.subplots(figsize = (7, 4))
ax0.fill_between(var_brake, out_poor, facecolor = 'b', alpha = 0.7) 
ax0.plot(var_brake, set_brake_poor, 'b', linestyle ='--')
ax0.fill_between(var_brake,  out_strong, facecolor='g', alpha = 0.7)
ax0.plot(var_brake, set_brake_strong, 'g', linestyle = '--')
ax0.set_title("Fren çıkışı")


out_brake = np.fmax(out_poor, out_strong)
defuzzified = fuzz.defuzz(var_brake, out_brake, 'centroid') 
result = fuzz.interp_membership(var_brake, out_brake, defuzzified)
