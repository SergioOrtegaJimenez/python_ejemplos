class LigaDeLaJusticiaDeZackSnyder:
    contador_miembros = 0 # Inicializamos a 0 el contador de miembros de la Liga
    trinidad = 0 # Inicializamos a 0 el contador de miembros de la Trinidad de la Liga (Batman, Superman o Wonder Woman)

# Definimos el metodo constructor de la clase, el cual espera recibir 2 valores desde los objetos (nombre y nombre_real)
    def __init__(self, nombre, nombre_real):
        LigaDeLaJusticiaDeZackSnyder.contador_miembros += 1 # Se incrementa en 1 el contador cada vez que se acceda a la clase
        self._id = LigaDeLaJusticiaDeZackSnyder.contador_miembros # Se crea el atributo "id" y se le asigna el valor que tenga el contador de miembros
        self._nombre = nombre
        self._nombre_real = nombre_real
        if nombre == 'Batman' or nombre == 'Superman' or nombre == 'Wonder Woman': # Bucle que incrementa el contador de los miembros de la Trinidad de la Liga solo si recibe el nombre de estos
            LigaDeLaJusticiaDeZackSnyder.trinidad += 1

    def get_nombre(self): # Metodo que permite leer el valor del atributo
        return self._nombre

    def set_nombre(self, nombre): # Metodo que permite modificar el valor del atributo
        self._nombre = nombre

    def get_nombre_real(self): # Metodo que permite leer el valor del atributo
        return self._nombre_real

    def set_nombre_real(self, nombre_real): # Metodo que permite modificar el valor del atributo
        self._nombre_real = nombre_real

    def mostrar_miembros(self): # Metodo que nos muestra los valores recibidos en el constructor de la clase
        print (f'Miembro: {self._id}, Héroe: {self._nombre},'
               f' Nombre Real del Héroe: {self._nombre_real}')





# Creamos el objeto 1 y le asignamos los 2 valores que espera recibir el constructor de la clase (nombre y nombre_real)
miembro1 = LigaDeLaJusticiaDeZackSnyder('Batman', 'Bruce Wayne')
miembro1.mostrar_miembros() # Llamamos al metodo "mostrar_miembros()"

# Creamos el objeto 2 y le asignamos los 2 valores que espera recibir el constructor de la clase (nombre y nombre_real)
miembro2 = LigaDeLaJusticiaDeZackSnyder('Superman', 'Clark Kent/Kal-El')
miembro2.mostrar_miembros() # Llamamos al metodo "mostrar_miembros()"

# Creamos el objeto 3 y le asignamos los 2 valores que espera recibir el constructor de la clase (nombre y nombre_real)
miembro3 = LigaDeLaJusticiaDeZackSnyder('Wonder Woman', 'Diana Prince')
miembro3.mostrar_miembros() # Llamamos al metodo "mostrar_miembros()"

# Creamos el objeto 4
#miembro4 = LigaDeLaJusticiaDeZackSnyder('Aquaman', 'Arthur Curry')
#miembro4.mostrar_miembros()

# Creamos el objeto 5
#miembro5 = LigaDeLaJusticiaDeZackSnyder('Flash', 'Barry Allen')
#miembro5.mostrar_miembros()

# Creamos el objeto 6
#miembro6 = LigaDeLaJusticiaDeZackSnyder('Cyborg', 'Victor Stone')
#miembro6.mostrar_miembros()

# Creamos el objeto 7
#miembro7 = LigaDeLaJusticiaDeZackSnyder('Green Lantern', 'John Stewart')
#miembro7.mostrar_miembros()

# Creamos el objeto 8
#miembro8 = LigaDeLaJusticiaDeZackSnyder('Martian Manhunter', 'Jonn Jonzz')
#miembro8.mostrar_miembros()

# Resultados de los contadores
if LigaDeLaJusticiaDeZackSnyder.trinidad == 3 and LigaDeLaJusticiaDeZackSnyder.contador_miembros == 3:
    print (f'\nMiembros de la Liga de la Justicia: {LigaDeLaJusticiaDeZackSnyder.contador_miembros} héroes.'
           f' ¡¡ES LA TRINIDAD!! #RestoreTheSnyderVerse')
if LigaDeLaJusticiaDeZackSnyder.trinidad <= 2:
    print(f'\nMiembros de la Liga de la Justicia: {LigaDeLaJusticiaDeZackSnyder.contador_miembros} héroes.'
          f'#RestoreTheSnyderVerse')
if LigaDeLaJusticiaDeZackSnyder.trinidad == 3 and LigaDeLaJusticiaDeZackSnyder.contador_miembros > 3:
    print(f'\nMiembros de la Liga de la Justicia: {LigaDeLaJusticiaDeZackSnyder.contador_miembros} héroes.'
          f' La Trinidad tiene refuerzos. #RestoreTheSnyderVerse')