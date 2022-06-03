class Alumnos:
    def __init__(self, nombre, edad, año):
        self.nombre = nombre
        self.edad = edad
        self.año = año

    def descripcion(self):
        return 'El nombre del alumno es: {}\nLa edad del alumno es: {}\nEl año que cursa es: {}'.format(self.nombre, self.edad, self.año)


print("Ingrese el nombre del alumno: ")
nombre = input()
print("Ingrese la edad del alumno: ")
edad = input()
print("Ingrese el año que cursa: ")
año = input()
alumno1 = Alumnos(nombre, edad, año)

print(alumno1.descripcion())
