
class Hotel: # Se crea una nueva clase "Hotel"
    
    def __init__(self, numero_max_huespedes, lugares_estacionamiento): #Usamos el método especial __init__ para definir el estado INICIAL DE LA INSTANCIA. Recibe como primer parametro OBLIGATORIO "self" que es uan referencia la instancia.
        self.numero_max_huespedes = numero_max_huespedes        
        self.lugares_estacionamiento = lugares_estacionamiento
        self.huespedes = 0
    
    def anadir_huespedes(self,cantidad_huespedes):
        self.huespedes += cantidad_huespedes # += se suma "cantidad_huespedes" al atributo "huespedes" del objeto "hotel1"

    def checkout(self,cantidad_huespedes):
        self.huespedes -= cantidad_huespedes # -= se resta "cantidad_huespedes" al atributo "huespedes" del objeto "hotel1"
    
    def ocupacion_total(self):
        return self.huespedes

hotel1 = Hotel(50, 20) # Una vez tenemos la clase llamada Hotel se genera una instancia llamando al constructor de la clase (como una función)
hotel2 = Hotel(100, 120) # Una vez tenemos la clase llamada Hotel se genera una instancia llamando al constructor de la clase (como una función)
print(f'El hotel1 tiene una ocupación máxima de {hotel1.numero_max_huespedes} huéspedes y dispone de {hotel1.lugares_estacionamiento} plazas de estacionamiento.') #muestra el valor del atributo lugares_estacionamiento de la instancia hotel1
print(f'El hotel1 tiene una ocupación máxima de {hotel2.numero_max_huespedes} huéspedes y dispone de {hotel2.lugares_estacionamiento} plazas de estacionamiento.') #muestra el valor del atributo lugares_estacionamiento de la instancia hotel2

hotel1.anadir_huespedes (int(input('Introduzca el número de huéspedes a añadir al hotel1:')))
hotel1.checkout (int(input('Introduzca el número de checkouts del hotel1:')))
print(f'La ocupación actual del hotel1 es {hotel1.ocupacion_total()}')