from Ataques.Ataque import Ataque;
import random;

class RayoVeloz(Ataque):
    def __init__(self):
        self.damage = 3;
        self.addsHealth2attacker = False;
        self.extraDamage = 1;
    