# Definimos la clase
class Coche:
    def __init__(self, marca, modelo): # Definimos metodo constructor
        self._marca = marca
        self._modelo = modelo

    # PRIMERA OPCION de encapsulamiento de los metodos get y set
    def get_marca(self): # Para leer el valor del atributo
        return self._marca

    def set_marca(self, marca): # Para modificar el valor del atributo (OPCION 1)
        self._marca = marca

    # SEGUNDA OPCION de encapsulamiento de los metodos get y set
    @property
    def modelo(self): # Para leer el valor del atributo
        return self._modelo

    @modelo.setter
    def modelo(self, modelo): # Para modificar el valor del atributo (OPCION 2)
        self._modelo = modelo

    # Metodo para mostrar los resultados
    def conducir(self):
        print (f'Conduciendo el coche de MARCA {self._marca}, '
               f'MODELO {self._modelo}')


# Creamos el objeto con valores por defecto
coche1 = Coche('Ford', 'Mustang')

# Llamamos al metodo para comprobar resultados
coche1.conducir()

# OPCION 1 para modificar un valor mediante encapsulamiento
coche1.set_marca('Peugeot')

# OPCION 2 para modificar un valor mediante encapsulamiento
coche1.modelo = '308'

# Llamamos al metodo para comprobar resultados de nuevo
coche1.conducir()