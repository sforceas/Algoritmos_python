"""
Complegidad: 
"""

def mochila(tamano_mochila, pesos, valores, n):
    
    if n == 0 or tamano_mochila == 0: #caso base para la recursividad. No quedan mas elementos o la mochila esta llena
        print('n==0, tamano_mochila==0')
        return 0
    
    if pesos[n-1]>tamano_mochila: #si el peso del elemento no cabe dentro del espacio disponible
        
        return mochila(tamano_mochila,pesos, valores, n-1) #probar el siguiente elemento de manera recursiva
    
    return max (valores[n-1] + mochila(tamano_mochila - pesos [n-1], pesos, valores, n-1), mochila(tamano_mochila,pesos, valores, n-1)) #se decide meter el objeto si su valor es el maximo

if __name__=='__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_mochila = 5
    n = len(valores)

    resultado = mochila(tamano_mochila, pesos, valores,n)
    print(f'El valor máximo que cabe en la mochila es {resultado}')