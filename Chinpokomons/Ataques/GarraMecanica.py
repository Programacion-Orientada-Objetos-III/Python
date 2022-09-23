from Ataques.Ataque import Ataque;
import random;

class GarraMecanica(Ataque):
    def __init__(self):
        self.damage = 2;
        self.addsHealth2attacker = False;
        self.extraDamage = 2;
    