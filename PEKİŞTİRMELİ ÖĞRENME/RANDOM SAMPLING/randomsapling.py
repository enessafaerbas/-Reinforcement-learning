# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 09:51:41 2021

@author: User
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

import random

N=10000
d=10
toplam=0
secilen= []
for n in range(0,N):
    ad=random.randrange(d)
    secilen.append(ad)
    odul= veriler.values[n,ad]
    toplam = toplam + odul
    
    
plt.hist(secilen)
plt.show()