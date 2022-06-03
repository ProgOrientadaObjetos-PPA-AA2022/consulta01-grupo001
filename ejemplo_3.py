class Persona:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
    def descripcion(self):
        return '{} estudia {} '.format(self.nombre, self.curso)
    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre, frase)


persona1 = Persona('Juan', 'Programacion')
print(persona1.descripcion())
print(persona1.comentario('Me gusta el curso'))

print("-----------------------------------------------------")

persona2 = Persona('Pedro', 'Matematicas')
print(persona2.descripcion())
print(persona2.comentario('Prefiero el curso de Matematicas'))