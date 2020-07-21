
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        #super().__init__(lado, lado) # Recomendable
        Rectangulo.__init__(self, lado, lado) # Otra forma

if __name__ == "__main__":
    rectangulo1 = Rectangulo(base = 3, altura = 4)
    print(rectangulo1.area())

    cuadrado1 = Cuadrado(lado = 5)
    print(cuadrado1.area())