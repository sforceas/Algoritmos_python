#La busqueda binaria es eficiente para buscar valores ORDENADOS
#Si la lista no esta ordenada, vale la pena realizar un algoritmo de ordenación si se repiten muchas veces la búsqueda -->amortizacion
import random

def busqueda_binaria(lista, comienzo, final, objetivo,contador=0):
    contador +=1
    if comienzo>final: #si el comienzo es mas grande que el final, apaga y vamonos
        return (False,contador)
    
    medio = (comienzo+final)//2 #dividimos la lista en 2 a partir de la posición "medio" con una division entera //
    
    if lista[medio] == objetivo: #encontró el objetivo 
        return (True,contador)
        
    elif lista[medio] < objetivo: #el objetivo es mayor que el medio, por lo que está en la parte "derecha" de la lista
        return busqueda_binaria(lista, medio+1, final, comienzo, contador)  #el nuevo comienzo para la proxima iteracion es medio+1
        
    else: #el objetivo es menor que el medio, por lo que está en la parte "izquierda" de la lista
        return busqueda_binaria(lista,comienzo,medio-1,objetivo, contador) #el nuevo comienzo para la proxima iteracion es medio-1



def busqueda_lineal(lista,objetivo,contador=0):
    encontrado = False

    for elemento in lista:            # Conmplejidad lineal: O(n). Unico loop que se repite n veces, siendo n un input directo.
        contador +=1
        if elemento == objetivo:
            encontrado = True
            break #se sale del loop si se encuentra
    return (encontrado,contador)





if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño será la lista?'))
    objetivo = int(input('Que numero quieres encontrar?'))

lista = sorted([random.randint(0,10000)for i in range(tamano_de_lista)])  #genera y ordena con sorted() una lista con valores aleatorios entre 0 y 100 con el tamaño de la lista.

print(lista)

(encontrado,contador) = busqueda_lineal(lista,objetivo)
print(f'Busqueda lineal: El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista. Se han realizado {contador} iteraciones.')

(encontrado,contador) = busqueda_binaria(lista, 0, len(lista), objetivo) 
print(f'Busqueda binaria: El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista. Se han realizado {contador} iteraciones.')

