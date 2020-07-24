import random

def ordenamiento_de_burbuja(lista,contador=0):   ### Complejidad: O(n) * O(n-i-1) = O(n*n) + O(n**2) --> Crecimiento cuadrático
    n = len(lista) #longitud de la lista para obtener

    for i in range(n): #iterar la busqueda el numero de elementos que mide la lista
        for j in range(0, n-i-1): # cada vez que se realiza un recorrido completo de la lista, al asgurarnos que el valor maximo ha quedado al final, podemos quitarle el ultimo paso a laproxima iteracion (n-1)
             contador +=1
             if lista[j] > lista [j+1]: #comparamos el índice con el que viene después si es mas grande, realizamos el intercambio
                lista[j], lista [j+1] = lista[j+1], lista[j] #python tiene esta funcionalidad para intercambiar variables llamada SWAP
    return lista, contador




if __name__ == '__main__':
 tamano_de_lista = int(input('De que tamaño será la lista?'))
 
 lista = [random.randint(0,100)for i in range(tamano_de_lista)]  #genera una lista con valores aleatorios entre 0 y 100 con el tamaño de la lista
 print(lista)
 (lista_ordenada, contador) = ordenamiento_de_burbuja(lista)
 print(lista_ordenada)
 print(f'Iteraciones: {contador}')

