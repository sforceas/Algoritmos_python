import random

def busqueda_lineal(lista,objetivo):
    match = False

    for elemento in lista:            # Conmplejidad lineal: O(n). Unico loop que se repite n veces, siendo n un input directo.
        if elemento == objetivo:
            match = True
            break #se sale del loop si se encuentra
    return match

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño será la lista?'))
    objetivo = int(input('Que numero quieres encontrar?'))

lista = [random.randint(0,100)for i in range(tamano_de_lista)]  #genera una lista con valores aleatorios entre 0 y 100 con el tamaño de la lista.

print(lista)
encontrado = busqueda_lineal(lista,objetivo)
print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista.')



