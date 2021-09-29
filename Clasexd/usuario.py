"""clase usuario que recibe dos parametros y un metodo
, ID, Nombre como parametro: saludar: hola
"""
import random
class Usuario():
    def __init__(self, ID, Nombre):
        self.id = ID
        self.nombre = Nombre
        return
    def saludar(self):
        return "Hola"
class Cansones():
    def __init__(self,name):
        self.name=name
    def calvazos(self):
        return "te has ganado un calvazo"

def estAnimo():
    estado = ["Alegre", "Triste", "Dichoso", "Rabioso"]
    return random.choice(estado)
print(estAnimo())