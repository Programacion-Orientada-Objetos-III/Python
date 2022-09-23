from Ataques.Ataque import Ataque;
import random;

class Zapatazo(Ataque):
    def __init__(self):
        self.damage = 1;
        self.addsHealth2attacker = False;
        self.extraDamage = 3;
    @property
    def damage(self):
        return self.__damage;
    
    def realizarAtaque(self, chinpokomonAtacante, chinpokomonDefensor.vida):
        #1 Posibilidad entre 10 de que sea true (10%)
        golpeCritico = random.choice([True, False]);
        if(golpeCritico):
            chinpokomonDefensor.dealDamage(self.damage);
        super.realizarAtaque(chinpokomonAtacante,chinpokomonDefensor);