###REVISAR CON ORDENAMIENTO_MEZCLA_TUTOR

import random

def ordenamiento_mezcla(lista):   ### Complejidad:
    #La division de las listas tiene un crecimiento logaritmico
    if len(lista)>1: #si las listas son mayores a 1 se dividen por la mitad en dos parts
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*'* 5, derecha)
    
        #llamada recursiva en cada mitad de la lista para ir dividiendo y ordenando las sublistas dsde menor a mayor longitud hasta su caso base len(lista) = 1
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        #iteradores para recorrer las sublistas
        i = 0
        j = 0
        #iterador para la lista general
        k = 0

        #cuando la llamada recursiva llega a su caso base, ejecuta los whiles y va retrocediendo frame por frame

        while i < len(izquierda) and j < len(derecha): #nos aseguramos que podamos comparar ambos valores
            if izquierda[i] < derecha[j]: #si el indice i de la lita izquierda es menor que el indice j de la lista derecha
                lista[k] = izquierda[i] #Reconstruyendo la lista poco a poco de menor a mayor, por lo que se pone el valor menor de la comparacion
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1      
            k+=1 #para que while no se vaya al infinito <--CUIDADO CON LA INDENTACION QUE TE PUEDE FASTIDIAR EL PROGRAMA
        
        #si ya no puede comparar porque se acabo la otra lista, es porque ya está ordenada asi que copia directamente la lista
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k+=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j+=1
            k+=1
        
        print (f'izquierda {izquierda}, derecha {derecha}')
        print (lista)
        print ('-'*30)
    
    return lista




if __name__ == '__main__':
 tamano_de_lista = int(input('De que tamaño será la lista?'))
 lista = [random.randint(0,10)for i in range(tamano_de_lista)]  #genera una lista con valores aleatorios entre 0 y 10 con el tamaño de la lista
 print('Lista original: ')
 print(lista)
 print ('='*50)
 lista_ordenada = ordenamiento_mezcla(lista)
 print('Lista ordenada: ')
 print(lista_ordenada)
 print ('='*50)

