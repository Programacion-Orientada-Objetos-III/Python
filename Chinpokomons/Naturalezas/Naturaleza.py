from INaturaleza import INaturaleza;
class Naturaleza(INaturaleza):
    def __init__(self):
        self.name = None;
    @property 
    def name(self):
        return self.name;
    @name.setter
    def name(self,name2Set):
        self.__name = name2Set;
    
    def tieneVentajaContra(self,naturaleza):
        False;
        