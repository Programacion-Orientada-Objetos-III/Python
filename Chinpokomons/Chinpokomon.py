import random;
from Chinpokomons.Ataques.Ataque import Ataque;
class Chinpokomon:
    def __init__(self):
        self.vida = None;
        self.nombre = None;
        self.isDeath = None;
        self.ataques = [];
    
    @property
    def vida(self):
        return self.__vida;
    @property
    def nombre(self):
        return self.__nombre;
    @property
    def isDeath(self):
        return self.__isDeath;
    @property
    def ataques(self):
        return self.__ataques;
    @vida.setter
    def vida(self,vida):
        self.__vida = vida;
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre;
    @isDeath.setter
    def isDeath(self,isDeath):
        self.__isDeath = isDeath;
    @ataques.ataques
    def ataques(self,ataques):
        self.__ataques = ataques;
    def addLife(self,life):
        self.vida += life;
    def dealDamage(self,damage):
        if(self.vida - damage < 0):
            self.isDeath(True);
            self.vida(0);
            print("El chinpokomon " + self.nombre + " murion.")
        else:
            self.vida(self.vida-damage)
            print("El chinpokomon " + self.nombre + " tiene "+ self.vida + " de vida");
    def atacar(self,chinpokomon):
        max = len(self.ataques);
        random = random.randint(0, max-1)
        ataque = self.ataques[random];
        ataque.realizarAtaque();