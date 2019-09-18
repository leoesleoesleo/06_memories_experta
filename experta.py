# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:12:39 2019

@author: leonardo.patino
"""

from random import choice
from experta import *
import pandas as pd


df = pd.read_csv('dataset.csv',delimiter=';')


class Light(Fact):
    """ info """
    pass

class RobotCrossStreet(KnowledgeEngine):
    
    @Rule(Light(param='lete'))
    def regla1(self):
        p = 'lete'
        s = 'Naranja'
        c = 'las llamadas y las transacciones se encuentran por encima de lo normal'
        print("Parametro: %s Alerta: %s Descripción: %s" % (p, s, c))
    
    @Rule(Light(param='leve'))
    def regla2(self):
        p = 'leve'
        s = 'Naranja'
        c = 'las llamadas y los volumenes de planta se encuentran por encima de lo normal'
        print("Parametro: %s Alerta: %s Descripción: %s" % (p, s, c))  
    
    @Rule(Light(param='le'))
    def regla3(self):
        p = 'le'
        s = 'Verde'
        c = 'las llamadas se encuentran por encima de lo normal'
        print("Parametro: %s Alerta: %s Descripción: %s" % (p, s, c))      
    
    @Rule(Light(param='te'))
    def regla4(self):
        p = 'te'
        s = 'Amarillo'
        c = 'las transacciones se encuentran por encima de lo normal'
        print("Parametro: %s Alerta: %s Descripción: %s" % (p, s, c))

    @Rule(Light(param='ve'))
    def regla5(self):
        p = 've'
        s = 'Verde'
        c = 'los volumenes de planta se encuentran por encima de lo normal'
        print("Parametro: %s Alerta: %s Descripción: %s" % (p, s, c))

    @Rule(Light(param='ld'))
    def regla6(self):
        p = 'ld'
        s = 'Verde'
        c = 'las llamadas se encuentran por debajo de lo normal'
        print("Parametro: %s Alerta: %s Descripción: %s" % (p, s, c))  

    @Rule(AS.light << Light(param=L('vd') | L('td')))
    def regla7(self):
        p = 'vt'
        s = 'Verde'
        c = 'Los volumenes de planta y las transacciones tienen un bajón anormal'
        print("Parametro: %s Alerta: %s Descripción: %s" % (p, s, c))
        
engine = RobotCrossStreet()
engine.reset()

fila = 0 
n = len(df)

while fila < n:
    engine.declare(Light(param=choice([df.iloc[fila, 5]])))
    engine.run()
    if df.iloc[fila, 5] != 'na':
        print("Intervalo: ",df.iloc[fila, 1])
    fila = fila + 1


        