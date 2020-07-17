
class automovil: 

    def __init__ (self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'  #variable privada empieza por un _
        self._motor = Motor(cilindros=4)
    
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina (10)

        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'en movimiento'


class Motor:

    def __init__ (self, cilindros, tipo='gasolina'): #tipo es un default keyword
        self.cilindro = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self,cantidad):
        pass
