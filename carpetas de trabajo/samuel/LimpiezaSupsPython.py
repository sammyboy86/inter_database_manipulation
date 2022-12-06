#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

data=pd.read_csv('dataMonet.csv')  

#estas son las columnas que queremos modificar
porMod=['appearance.height','appearance.weight','work.occupation','biography.fullName','biography.alterEgos','biography.firstAppearance','biography.aliases']

#cambiamos todas las comas de cada columna obtenida por "-",
#cada columna va en un arreglo y eso dentro de otro arreglo llamado results
results=[]
for j in porMod:    
    col=data[j]
    resAux=[]
    for i in col:
        resAux.append(str(i).replace(",", "-" )) 
    results.append(resAux)

#cambiamos columnas viejas por nuevas
dataAux=data
cont=0
for h in porMod:    
    dataAux[h] = results[cont]
    cont=cont+1


#lo pasamos a un csv
dataAux.to_csv('../supsLimpio.csv',header=True,index=False)

