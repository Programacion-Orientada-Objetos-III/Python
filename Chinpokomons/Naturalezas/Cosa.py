from Naturaleza import Naturaleza;

class Cosa(Naturaleza):
    def __init__(self):
        self.name = "Cosa";
    @property
    def name(self):
        return self.__name;
    def tieneVentajaContra(self,naturaleza):
        return naturaleza.name == "Robot";