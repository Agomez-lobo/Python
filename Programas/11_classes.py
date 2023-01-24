### Classes ###

class Persona:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.__pos = "Privada"

    def caminar(self):
        print(f"{self.name} está caminando." )

    def get_pos(self):
        return self.__pos

my_person = Persona('Alejandro', 'Gomez-Lobo')

print(f"{my_person.name} {my_person.surname}")

my_person.caminar()

print(my_person.get_pos())