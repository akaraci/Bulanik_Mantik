# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:28:13 2022

@author: karaci
"""

import skfuzzy as fuzz
import skfuzzy.membership as mf
import numpy as np
import matplotlib.pyplot as plt

#----Değişkenler oluşturuluyor
var_model=np.arange(2002,2013,1)
var_km=np.arange(0,100001,1)
var_fiyat=np.arange(0,40001,1)

#----Model için Üyelik Fonksiyonları Tanımlanıyor
set_model_dusuk=mf.trimf(var_model, [2002,2002,2007])
set_model_orta=mf.trimf(var_model, [2002,2007,2012])
set_model_yuksek=mf.trimf(var_model, [2007, 2012, 2012])
#----Model için Bulanık Kümeler Çizdiriliyor
fig,(ax0,ax1,ax2,ax3,ax4)=plt.subplots(nrows=5,figsize=(15,20))
ax0.plot(var_model,set_model_dusuk,'r',linewidth=2, label='Düşük')
ax0.plot(var_model,set_model_orta,'g',linewidth=2, label='Orta')
ax0.plot(var_model,set_model_yuksek,'b',linewidth=2, label='Yüksek')
ax0.set_title("Model")
ax0.legend()


#----Kilometre için Üyelik Fonksiyonları Tanımlanıyor
set_km_dusuk=mf.trimf(var_km, [0,0,50000])
set_km_orta=mf.trimf(var_km, [0,50000,100000])
set_km_yuksek=mf.trimf(var_km, [50000, 100000, 100000])
#----Kilometre için Bulanık Kümeler Çizdiriliyor
ax1.plot(var_km,set_km_dusuk,'r',linewidth=2, label='Düşük')
ax1.plot(var_km,set_km_orta,'g',linewidth=2, label='Orta')
ax1.plot(var_km,set_km_yuksek,'b',linewidth=2, label='Yüksek')
ax1.set_title("Kilometre")
ax1.legend()


#----Kilometre için Üyelik Fonksiyonları Tanımlanıyor
set_fiyat_dusuk=mf.trimf(var_fiyat, [0,0,20000])
set_fiyat_orta=mf.trimf(var_fiyat, [0,20000,40000])
set_fiyat_yuksek=mf.trimf(var_fiyat, [20000, 40000, 40000])
#----Kilometre için Bulanık Kümeler Çizdiriliyor
ax2.plot(var_fiyat,set_fiyat_dusuk,'r',linewidth=2, label='Düşük')
ax2.plot(var_fiyat,set_fiyat_orta,'g',linewidth=2, label='Orta')
ax2.plot(var_fiyat,set_fiyat_yuksek,'b',linewidth=2, label='Yüksek')
ax2.set_title("Kilometre")
ax2.legend()

#Hesaplama Yapılacak Girişler belirleniyor
input_model=2011
input_km=25000

#Herbir Girişin giriş bulanık kümelerine üyelik dereceleri hesaplanıyor
model_fit_dusuk=fuzz.interp_membership(var_model,set_model_dusuk,input_model)
model_fit_orta=fuzz.interp_membership(var_model,set_model_orta,input_model)
model_fit_yuksek=fuzz.interp_membership(var_model,set_model_yuksek,input_model)
#Üyelik dereceleri grafik üzerinde gösteriliyor
#         [x1,x2],[y1,y2] şeklinde düz çizgi verileri verilmelidir.
ax0.plot([input_model,input_model],[0,model_fit_dusuk],'r',linewidth=1, linestyle='--')
ax0.plot([2002,input_model],[model_fit_dusuk,model_fit_dusuk],'r',linewidth=1, linestyle='--')
ax0.plot([input_model,input_model],[0,model_fit_orta],'r',linewidth=1, linestyle='--')
ax0.plot([2002,input_model],[model_fit_orta,model_fit_orta],'r',linewidth=1, linestyle='--')
ax0.plot([input_model,input_model],[0,model_fit_yuksek],'r',linewidth=1, linestyle='--')
ax0.plot([2002,input_model],[model_fit_yuksek,model_fit_yuksek],'r',linewidth=1, linestyle='--')

km_fit_dusuk=fuzz.interp_membership(var_km,set_km_dusuk,input_km)
km_fit_orta=fuzz.interp_membership(var_km,set_km_orta,input_km)
km_fit_yuksek=fuzz.interp_membership(var_km,set_km_yuksek,input_km)
#Üyelik dereceleri grafik üzerinde gösteriliyor
#         [x1,x2],[y1,y2] şeklinde düz çizgi verileri verilmelidir.
ax1.plot([input_km,input_km],[0,km_fit_dusuk],'r',linewidth=1, linestyle='--')
ax1.plot([0,input_km],[km_fit_dusuk,km_fit_dusuk],'r',linewidth=1, linestyle='--')
ax1.plot([input_km,input_km],[0,km_fit_orta],'r',linewidth=1, linestyle='--')
ax1.plot([0,input_km],[km_fit_orta,km_fit_orta],'r',linewidth=1, linestyle='--')
ax1.plot([input_km,input_km],[0,km_fit_yuksek],'r',linewidth=1, linestyle='--')
ax1.plot([0,input_km],[km_fit_yuksek,km_fit_yuksek],'r',linewidth=1, linestyle='--')

#Kurallar oluşturuluyor ve uygulanıyor Mamdani
rule1 = np.fmin(np.fmin(model_fit_dusuk, km_fit_yuksek), set_fiyat_dusuk)
rule2 = np.fmin(np.fmin(model_fit_orta, km_fit_orta), set_fiyat_orta)
rule3 = np.fmin(np.fmin(model_fit_yuksek, km_fit_dusuk), set_fiyat_yuksek)
print(max(rule3))
 
ax3.plot(var_fiyat,rule1,'r', linestyle='--', linewidth=1, label='Rule-1')
ax3.plot(var_fiyat,rule2, 'b', linestyle='-.', linewidth=2, label='Rule-2')
ax3.plot(var_fiyat,rule3, 'g', linestyle=':', linewidth=2, label='Rule-3')
ax3.set_title("Her bir kuraldan elde edilen çıkış kümeleri")
ax3.legend()


#Her bir kuraldan elde edilen Çıkışların Maksimumu Alınıyor
out1=np.fmax(rule1,rule2)
out_set_final=np.fmax(out1,rule3) #Nihai bulanık çıkış kümemiz
ax4.fill_between(var_fiyat,out_set_final, 'b', linestyle=':', linewidth=2, label='out')
ax4.set_title("Çıkış-Bulanık Küme Birleşimi")

#Durulama İşlemi Yapılıyor
#Durulama Yöntemleri
# 'centroid' — Centroid of the area under the output fuzzy set
# 'bisector' — Bisector of the area under the output fuzzy set
# 'mom' — Mean of the values for which the output fuzzy set is maximum
# 'lom' — Largest value for which the output fuzzy set is maximum
# 'som' — Smallest value for which the output fuzzy set is maximum

defuzzified_centroid = fuzz.defuzz(var_fiyat, out_set_final, 'centroid') 
print("Fiyat(centroid)=",defuzzified_centroid)

defuzzified_bisector = fuzz.defuzz(var_fiyat, out_set_final, 'bisector') 
print("Fiyat(bisector)=",defuzzified_bisector)

defuzzified_mom = fuzz.defuzz(var_fiyat, out_set_final, 'mom') 
print("Fiyat(mom)=",defuzzified_mom)

defuzzified_lom = fuzz.defuzz(var_fiyat, out_set_final, 'lom') 
print("Fiyat(lom)=",defuzzified_lom)

defuzzified_som = fuzz.defuzz(var_fiyat, out_set_final, 'som') 
print("Fiyat(som)=",defuzzified_som)

hangisi=defuzzified_centroid
result = fuzz.interp_membership(var_fiyat, out_set_final, hangisi)
ax4.plot([0,hangisi],[result,result],'r')
ax4.plot([hangisi,hangisi],[0,result],'r')


