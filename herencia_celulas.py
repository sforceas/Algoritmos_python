"""
    En este programa se crea un superclase Celula cuyos atributos son el diámetro, su funcionamiento y el estado en el que se encuentra.
    De esta superclase nacen dos subclases con diferentes métodos en función de sus especializaciones: 
    - Neurona: es una Celula que además tiene una longitud y un número de dendritas(conexines con otras neuronas). Dispone de un método para calcular su volúmen.
    - Hematocito: es una Celula que además se encuentra en una determinada concentración en sangre. Dispone de un método que evalua esta concentración.

"""
class Celula:

    def __init__(self,diametro,funcionamiento,estado):
        self.diametro = diametro #en micrómetros
        self.funcionamiento = funcionamiento #normal, cancerosa
        self.estado=estado #viva, muerta
    
    def area(self):
        return f'Area: {2*3.14*(self.diametro/2)**2} um^2.'

class Neurona(Celula):

    def __init__(self,diametro,funcionamiento,estado,longitud,num_dendritas):
        super().__init__(diametro,funcionamiento,estado) #atributos propios de la superclase celula comunes con otras subclases
        self.longitud = longitud #atributos únicos de esta subclase en concreto
        self.num_dendritas = num_dendritas #atributos únicos de esta subclase en concreto
    
    def volumen(self): #Método único de Neurona que valora si la concentración de hematocitos en sangre está por debajo de un umbral fijo.
        return f'Volumen: {self.diametro * self.longitud} um^3'  

class Hematocito(Celula):

    def __init__(self,diametro,funcionamiento,estado,concentracion):
        super().__init__(diametro,funcionamiento,estado) #atributos propios de la superclase celula comunes con otras subclases
        self.concentracion = concentracion #atributos únicos de esta subclase en concreto
    
    def valorar_concentracion(self): #Método único de Hematocito que valora si la concentración de hematocitos en sangre está por debajo de un umbral fijo.
        umbral_concentracion_hematocitos = 300
        if self.concentracion < umbral_concentracion_hematocitos:
            return 'Concentración baja.'
        else:
            return 'Concentración correcta.'

if __name__=="__main__":

    #Se crean ambas instancias. Vease que al tratarse de subclases diferentes pero con la misma superclase comparten las variables de ésta pero difieren en las suyas propias.
    neurona = Neurona(diametro=10, funcionamiento='cancerosa', estado='muerta', longitud=200, num_dendritas=25)
    hematocito = Hematocito(diametro=5, funcionamiento='normal', estado='viva', concentracion=400)


    #se imprimen determinados atributos y las respuestas de detrminados métodos para cada subclase en concreto.
    print(f'Estado de la neurona: {neurona.estado}, Funcionamiento: {neurona.funcionamiento}, {neurona.volumen()}, Número de dendritas: {neurona.num_dendritas}')
    print(f'Estado del hematocito: {hematocito.estado}, Funcionamiento: {hematocito.funcionamiento}, {hematocito.area()}, Concentración: {hematocito.concentracion} U/dL. {hematocito.valorar_concentracion()}')

