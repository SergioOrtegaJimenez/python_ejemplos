class Animal: # Esta es la clase padre o superclase
    def comer(self):
        print(f'Como muchas veces al dia (soy el metodo comer de la clase Padre)')

    def dormir(self):
        print(f'Duermo muchas horas (soy el metodo dormir de la clase Padre)')



class Perro(Animal): # Esta es una clase hija o subclase
    def hacer_sonido(self):
        print(f'Puedo ladrar (soy el metodo hacer_sonido de la clase Hija)')

    def dormir(self): # Con este metodo, realizamos SOBREESCRITURA ya que la clase Padre tambien tiene un metodo llamado de igual manera. Al hacer la llamada a este metodo desde un objeto de la clase Hija, se llamará al metodo de la clase Hija y no al de la clase Padre
        print(f'Duermo muchas horas (soy el metodo dormir de la clase Hija)')


class Gato(Animal): # Esta es una clase hija o subclase
    def hacer_sonido(self):
        print(f'Puedo maullar (soy el metodo hacer_sonido de la clase Hija)')


# Crear objeto de la clase Padre (clase Padre no puede acceder a metodos de clase Hija)
print(f'Clase Padre, soy un animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()


# Crear objeto de la clase Hija (clase Hija si puede acceder a metodos de clase Padre)
print(f'\nClase Hija, soy un perro')
perro1 = Perro()
perro1.hacer_sonido()
perro1.dormir() # Metodo de la SOBREESCRITURA
perro1.comer()