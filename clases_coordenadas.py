
class Coordenada:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distancia(self,otra_coordenada):
        x_diff = (self.x  - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
    
        return(x_diff + y_diff)**0.5 

if __name__ == '__main__':
    coord_1 = Coordenada(3,30)
    coord_2 = Coordenada(4,8)

    print (coord_1.distancia(coord_2)) #ejecuta el método distancia. Self = coord_1 y otra_coordenada =coord_2
    print (isinstance(coord_2, Coordenada)) # comprueba si coord_2 es una instancia de la clase coordenada (devuelve TRUE) -> Si da FALSE hay un error
    
