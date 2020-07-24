""" 
Este script genera una representación gráfica de los resultados obtenidos a partir de un ensayo de tracción de un material mediante una Maquina Universal de Ensayos. Los datos son exportados directamente a .csv
En futuras versiones, se incluirá una función que calcule las propiedades del material como el módulo elástico y su resistencia.
"""
from bokeh.plotting import figure, output_file, show
import pandas as pd #libreria pandas permite trabajar con hojas de datos tipo .csv 


def Leer_CSV(ruta): #lee los datos del csv y los almacena en una lista por cada columna.
        
    data = pd.read_csv(ruta) #obtiene el array completo de datos del archivo
    columna1=data['displacement'].tolist() #el encabezado de esta columna es "displacement"
    columna2=data['load'].tolist()  #el encabezado de esta columna es "load"
                  
    return columna1, columna2 #devuelve las listas correspondientes a cada columna

def graficar_linea (x_val, y_val): #genera un gráfico de línea con diferentes características
    output_file('Diagrama máquina de {ruta}.html')
    fig = figure()
    fig.line(x_val,y_val,line_width =3)
    fig.yaxis.axis_label = 'Carga (N)'
    fig.xaxis.axis_label = 'Desplazamiento (mm)'
    fig.title.text='Diagrama máqina (N/mm)'
    fig.toolbar_location='above'

    return fig #devuelve la figura completa con los datos


if __name__ =='__main__':
    
    ruta = input('Indique la ruta del achivo CSV: ')
    
    (desplazamiento_X, carga_Y)= Leer_CSV(ruta) #genera las listas correspondientes a las dos columnas
    show(graficar_linea (desplazamiento_X, carga_Y)) #recursividad que representa el resultado de la función que genera el gráfico



        

