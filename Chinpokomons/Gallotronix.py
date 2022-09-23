from Chinpokomons.Naturalezas.Animal import Animal;
from Chinpokomons.Chinpokomon import Chinpokomon;
class Gallotronix (Chinpokomon,Animal):
    def __init__(self):
        self.nombre = "Gallotronix";
    @property
    def nombre(self):
        return self.__nombre;