from Naturaleza import Naturaleza;

class Animal(Naturaleza):
    def __init__(self):
        self.name = "Animal";
    @property
    def name(self):
        return self.__name;
    def tieneVentajaContra(self,naturaleza):
        return naturaleza.name == "Cosa";