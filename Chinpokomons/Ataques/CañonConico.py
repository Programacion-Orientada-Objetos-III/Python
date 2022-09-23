from Ataques.Ataque import Ataque;
import random;

class CañonConico(Ataque):
    def __init__(self):
        self.damage = 4;
        self.addsHealth2attacker = False;
        self.extraDamage = 1;
    
    def realizarAtaque(self, chinpokomonAtacante, chinpokomonDefensor.vida):
        #1 Posibilidad entre 10 de que sea true (10%)
        golpeCritico = random.nextint(11) == 5;
        if(golpeCritico):
            chinpokomonDefensor.dealDamage(chinpokomonDefensor.vida/2);
        super.realizarAtaque(chinpokomonAtacante,chinpokomonDefensor);