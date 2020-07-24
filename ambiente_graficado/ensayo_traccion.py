""" 
Este script genera una representación gráfica de los resultados obtenidos a partir de un ensayo de tracción de un material mediante una Maquina Universal de Ensayos. Los datos son exportados directamente a .csv
En futuras versiones, se incluirá una función que calcule las propiedades del material como el módulo elástico y su resistencia.
"""
from bokeh.plotting import figure, output_file, show
import pandas as pd #libreria pandas permite trabajar con hojas de datos tipo .csv 
import statistics as st


class probeta:
    pass    

def leer_CSV (ruta): #lee los datos del csv y los almacena en una lista por cada columna.
                    #se pueden añadir más columnas repitiendo la línea columna(n) = data['cabezera de n'].tolist()
                    #estas columnas nuevas también se tienen que incluir en el return.

    data = pd.read_csv(ruta) #obtiene el array completo de datos del archivo
    columna1=data['displacement'].tolist() #el encabezado de esta columna es "displacement"
    columna2=data['load'].tolist()  #el encabezado de esta columna es "load"
                  
    return columna1, columna2 #devuelve las listas correspondientes a cada columna

def graficar_linea (x_val, y_val,titulo,etiqueta_eje_x,etiqueta_eje_y): #genera un gráfico de línea con diferentes características
    output_file(f'{titulo}.html')
    fig = figure()
    fig.line(x_val,y_val,line_width=3)
    fig.yaxis.axis_label = etiqueta_eje_y
    fig.xaxis.axis_label = etiqueta_eje_x
    fig.title.text= titulo
    fig.toolbar_location='above'

    return fig #devuelve la figura completa con los datos

def calcular_deformacion_tension (desplazamiento,carga, seccion,longitud):
    
    deformacion = (list(map(lambda x: 100*x /longitud, desplazamiento)))
    tension = (list(map(lambda x: 100*x /seccion, carga)))
    #deformacion = (desplazamiento/longitud)*100 # 100*(deltaL/L0) representa la deformación en %
    #tension = carga/seccion #N/mm2 = MPa

    return (deformacion, tension)

def calcular_modulo_elastico (deformacion,tension):
    
    #añadir try catch
    punto_inicial = float(input('Indique el valor de porcentual deformación donde iniciar el cálculo del módulo: '))
    punto_final = float(input('Indique el valor de porcentual deformación donde finalizar el cálculo del módulo: '))

    indice_inicial = buscar_indice(deformacion, punto_inicial)
    indice_final = buscar_indice(deformacion, punto_final)

    tension_acotada = tension[indice_inicial:indice_final]
    deformacion_acotada = deformacion[indice_inicial:indice_final]

    modulos = [i / j for i, j in zip(tension_acotada, deformacion_acotada)]

    modulo_elastico = st.mean(modulos)
    desvest_modulo_elastico = st.stdev(modulos)

    return modulo_elastico,  desvest_modulo_elastico

def buscar_indice (lista, objetivo):
     indice = min(range(len(lista)), key=lambda i: abs(lista[i]-objetivo))
     return indice


if __name__ == '__main__':
        
 ruta = input('Indique la ruta del achivo CSV: ')
 seccion = float(input('Indique la sección de la probeta en mm2: '))    
 longitud = float(input('Indique la longitud inicial de la probeta en mm: '))

 (desplazamiento, carga)= leer_CSV(ruta) #genera las listas correspondientes a las dos columnas
 
 (deformacion,tension) = calcular_deformacion_tension(desplazamiento,carga,seccion,longitud) 

 show(graficar_linea(desplazamiento, carga, 'Diagrama desplazamiento-carga', 'Desplazamiento (mm)','Carga (N)')) 
 show(graficar_linea(deformacion, tension, 'Diagrama tensión-deformacion', 'deformacion %','Tensión (MPa)')) 
 (modulo_elastico,desvest_modulo_elastico) = calcular_modulo_elastico(deformacion, tension)
 print(f'Modulo elástico: {round(modulo_elastico,1)} MPa. Desviación estandar: {round(desvest_modulo_elastico,1)}.')
 print(f'Resistencia máxima: {max(tension)}MPa.')