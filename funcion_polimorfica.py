class Animal:
    def hacer_ruido(self):
        print(f'Hago un ruido (metodo clase Padre Animal)')

class Perro(Animal):
    def hacer_ruido(self):
        print(f'Ladro (metodo clase Hija Perro)')

class Gato(Animal):
    def hacer_ruido(self):
        print(f'Maullo (metodo clase Hija Gato)')

# Definimos funcion polimorfica o "Duck Typing"
def hacer_ruido_animal(animal):
    print(f'\nEsto es una llamada a la funcion polimorfica')
    animal.hacer_ruido()

# Definimos los distintos objetos
animal1 = Animal()
perro1 = Perro()
gato1 = Gato()

# Llamada a funcion polimorfica
hacer_ruido_animal(animal1)
hacer_ruido_animal(perro1)
hacer_ruido_animal(gato1)