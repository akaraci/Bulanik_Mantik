# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 11:43:15 2022

@author: karaci
"""

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

#Bu bulanık kümenin nihai çıkış kümesi olduğunu varayıyoruz.
x=np.arange(2,4.5,0.1)
out_mfx = fuzz.trapmf(x, [2, 2.5, 3, 4.5])

# ------------------Durulaştırma değeri hesaplanıyor
defuzz_centroid = fuzz.defuzz(x, out_mfx, 'centroid')  
defuzz_bisector = fuzz.defuzz(x, out_mfx, 'bisector')
defuzz_mom = fuzz.defuzz(x, out_mfx, 'mom')
defuzz_som = fuzz.defuzz(x, out_mfx, 'som')
defuzz_lom = fuzz.defuzz(x, out_mfx, 'lom')

# Plot'ta dikey çizgi çizmek için gerekli bilgiler toplanıyor
labels = ['centroid', 'bisector', 'mean of maximum', 'min of maximum',
          'max of maximum']
xvals = [defuzz_centroid,
         defuzz_bisector,
         defuzz_mom,
         defuzz_som,
         defuzz_lom]
colors = ['r', 'b', 'g', 'c', 'm']

#Her bir durulaştırılmış değerin nihai çıkış bulanık kümesine üyeliği hesaplanıyor
ymax = [fuzz.interp_membership(x, out_mfx, i) for i in xvals]

plt.figure(figsize=(8, 5))

plt.plot(x, out_mfx, 'k')
#Dikey çizgi çiziliyor
for xv, y, label, color in zip(xvals, ymax, labels, colors):
    plt.vlines(xv, 0, y, label=label, color=color)
plt.ylabel('Fuzzy membership')
plt.xlabel('Universe variable (arb)')
plt.ylim(-0.1, 1.1)
plt.legend(loc=2)

plt.show()