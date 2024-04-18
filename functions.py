import pandas as pd
import numpy as np
import pymysql
import csv
import chardet
import pytz
import os

class Functions(object):
    def __init__(self):
        return 

    def ultrapassado(self, velocidade, pos_id):
        velocidade = int(velocidade)
        pos_id = int(pos_id)
        if velocidade > pos_id:
            if velocidade <= 100:
                tol = 1.1
                velocidadextol = pos_id * tol
                if velocidade > velocidadextol:
                    velocidadeExcedida = ((velocidade / pos_id) - 1) * 100
                    rounded_velocidadeExcedida = round(velocidadeExcedida, 2)
                    velocidadeExcedida_str = str(rounded_velocidadeExcedida) + '%'

                    return velocidadeExcedida_str
                else:
                    return ''
            else:
                tol = 1.07
                velocidadextol = pos_id * tol
                if velocidade > velocidadextol:

                    velocidadeExcedida = ((velocidade / pos_id) - 1) * 100
                    rounded_velocidadeExcedida = round(velocidadeExcedida, 2)
                    velocidadeExcedida_str = str(rounded_velocidadeExcedida) + '%'

                    return velocidadeExcedida_str
                else:
                    return ''
        else:
            return ''


    def velocidade_excedida(self,row):
        if row != '':
            return 'background-color: pink'
        else:
            return ''


    def add_km(self,valor):
        return f"{valor} km/h"