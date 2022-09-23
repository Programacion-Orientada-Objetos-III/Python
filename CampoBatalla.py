class CampoBatalla:
    def __init__(self,peleador1,peleador2):
        self.peleador1 = peleador1;
        self.peleador2 = peleador2;
        self.nextPeleador = self.peleador1;
        self.nextDefensor = self.peleador2;
    @property
    def peleador1(self):
        return self.__peleador1;
    @property
    def peleador2(self):
        return self.__peleador2;
    @property
    def nextPeleador(self):
        return self.__nextPeleador;
    @property
    def nextDefensor(self):
        return self.__nextDefensor;
    @nextPeleador.setter
    def nextPeleador(self,peleador):
        self.__nextPeleador = peleador;
    @nextDefensor.setter
    def nextDefensor(self,peleador):
        self.__nextDefensor = peleador;
    
    def changeRole(self):
        nextPeleadorAux = self.nextDefensor;
        nextDefensorAux = self.nextPeleador;
        self.nextDefensor(nextPeleadorAux);
        self.nextPeleador(nextDefensorAux);
    
    def comenzarPelea(self):
        while(not self.nextDefensor.isDeath and not self.nextPeleador.isDeath):
            self.nextPeleador.atacar(self.nextDefensor);
            self.changeRole();
        if self.peleador1.isDeath:
            print("El ganador es " + self.peleador2.name + " con "+ self.peleador1.vida + " de vida!")
        else:
            print("El ganador es " + self.peleador2.name + " con "+ self.peleador2.vida + " de vida!")