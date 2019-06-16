# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:59:13 2019

@author: Czarek
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import seaborn
from matplotlib import colors
import matplotlib.pyplot as plt
from scipy.stats import linregress
#Deklaracja danych
Date = []       
Time = []         
CO = []        
PT08 = []    
NMHC = []
C6H6 = []
  

#inicjacja pliku
plik = open('C:\\Users\\Czarek\\Desktop\\raport\\as.csv', 'rt')

dane = csv.reader(plik, delimiter=';')
next(dane)                # Opuszczamy pierwszy wiersz

#Załadowanie danych
for obserwacja in dane:   # Iterujemy po poszczególnych obserwacjach.
    dateS = datetime.datetime.strptime(str(obserwacja[0]), '%d/%m/%Y')
    timeS = datetime.datetime.strptime(str(obserwacja[1]), '%H.%M.%S')
    Date.append(dateS.date())
    Time.append(timeS.time())
    CO.append(float(obserwacja[2]))
    PT08.append(float(obserwacja[3]))
    NMHC.append(float(obserwacja[4]))
    C6H6.append(float(obserwacja[5]))
plik.close()

zmienne = {"CO(GT)":CO, "PT08.S1(CO)":PT08, "NMHC(GT)":NMHC,"C6H6":C6H6}

for nazwa,zmienna in zmienne.items():
    print()
    print("Zmienna:",nazwa)
    print("MIN:", min(zmienna))   
    print("MAX:", max(zmienna))
    print("ŚREDNIA:", np.mean(zmienna))
    print("MEDIANA:", np.median(zmienna))
    print("ZAKRES:", np.ptp(zmienna))
    print("ODCHYLENIE STANDARDOWE:", np.std(zmienna))
    print("WARIANCJA:", np.var(zmienna))
    print("PERCENTYL 90%:", np.percentile(zmienna,90) )
   

# Czcionka do wykresów, z polskimi znakami.
    plt.rc('font', family='Arial')

    # Wykres - histogram
    plt.hist(zmienna, 100)
    plt.title('Histogram dla: ' + nazwa)
    plt.xlabel('Przedział')
    plt.ylabel('Liczba obserwacji')
    plt.show()
    
    
   

    corr = dataset.corr()
    corr.style.background_gradient(cmap='coolwarm').set_precision(2)
    plt.imshow(corr,cmap='hot',interpolation='nearest')
    
       
    #korelacja miedzy CO(GT) a PT08.S1(CO)
    x = dataset["CO(GT)"]
    y = dataset["PT08.S1(CO)"]
    
    stats = linregress(x, y)
    
    m = stats.slope
    b = stats.intercept
    
    plt.scatter(x, y)
    plt.plot(x, m * x + b, color="red")
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    