class Animal:
    def hacer_ruido(self):
        print(f'Hago un ruido (metodo clase Padre)')

class Perro(Animal):
    def hacer_ruido(self):
        print(f'Ladro (metodo clase Hija Perro)')

class Gato(Animal):
    def hacer_ruido(self):
        print(f'Maullo (metodo clase Hija Gato)')



print(f'Clase Padre (Animal)')
animal1 = Animal()
animal1.hacer_ruido()

print(f'\nClase Hija (Perro)')
perro1 = Perro()
perro1.hacer_ruido()

print(f'\nClase Hija (Gato)')
gato1 = Gato()
gato1.hacer_ruido()