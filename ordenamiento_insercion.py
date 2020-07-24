# import math ...si es que se requieren raices cuadradas, o pi ...ejemplo: math.sqrt() o math.pi



numeros=[0,2,3,-7/4,3.2232323]    #<--------- si se quiere ordenar decimales, negativos o integers
#numeros=[int(x) for x in input('Introducir lista ').split()]  #<--- si se quiere introducir integers







sublistaOrdenada=[numeros[0]]
sublistaNoOrdenada=numeros[1:len(numeros)]



for i in range(len(numeros)-1):
    sublistaOrdenada.append(sublistaNoOrdenada[i]) #append agrega el ultimo valor del argumento a la variable antes del .
    
   
    if sublistaOrdenada[i]>sublistaOrdenada[i+1]:
        sublistaOrdenada[i],sublistaOrdenada[i+1]=sublistaOrdenada[i+1],sublistaOrdenada[i]

    

for i in range(len(numeros)-1):
    if sublistaOrdenada[(len(numeros)-1)-i]>sublistaOrdenada[(len(numeros)-1)-i-1]:
        pass
    else:
        sublistaOrdenada[(len(numeros)-1)-i],sublistaOrdenada[(len(numeros)-1)-i-1]=sublistaOrdenada[(len(numeros)-1)-i-1],sublistaOrdenada[(len(numeros)-1)-i]
print('---------------------------------------')
print('El arreglo de numeros a arreglar es:')
print (numeros)
print('---------------------------------------')
print('El ordenamiento por insercion arroja:  ')
print (sublistaOrdenada)
print('---------------------------------------')