# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:33:35 2021

@author: User
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

N=10000 # 10.000 tıklama
d=10 # toplam 10 ilan var
toplam=0 # toplam ödül
secilenler=[] 
birler=[0]*d
sifirlar=[0]*d
for n in range(0,N):
    ad = 0 # seçilen ilan
    max_th=0    
    for i in range(0,d):
        rasbeta=random.betavariate(birler[i]+1,sifirlar[i]+1)
        if rasbeta>max_th:
            max_th=rasbeta
            ad=i
       
    secilenler.append(ad)
    odul=veriler.values[n,ad]
    if odul==1:
        birler[ad]=birler[ad]+1
    else:
        sifirlar[ad]=sifirlar[ad]+1
    
    toplam=toplam+odul
print('Toplam odul :')
print(toplam)

plt.hist(secilenler)
plt.show()