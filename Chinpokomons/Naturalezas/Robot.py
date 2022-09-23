from Naturaleza import Naturaleza;

class Robot(Naturaleza):
    def __init__(self):
        self.name = "Robot";
    @property
    def name(self):
        return self.__name;
    def tieneVentajaContra(self,naturaleza):
        return naturaleza.name == "Animal";