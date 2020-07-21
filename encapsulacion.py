
class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self.__voto = None
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self.__region = region
        
        else:
            raise ValueError (f'La region {casilla.region} no esta en la lista.')

    @property
    def voto(self,voto):
        
        if  voto == ('Y' or 'N'):
                self.__voto = voto
                print('voto introducido correctamente.')
        else:
            print('Voto no válido.')

contrasena_administrador = 'password'

if input('Introduzca contraseña de administrador: ') == contrasena_administrador:
    casilla = CasillaDeVotacion(int(input('Introduzca el códifo de casilla: ')),input('Introduzca la regiones para esta casilla:'))
else: 
    print('Contraseña de administrador incorrecta.')

print(casilla.region)
casilla.region = input('Seleccione la región en la que votar: ')
casilla.voto = input('Introduzca la opción de su voto. Si (Y) o No (N): ')
print(f'Su voto para la region {casilla.region} es {casilla.voto}.')