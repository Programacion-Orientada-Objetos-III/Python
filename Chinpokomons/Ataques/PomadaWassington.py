from Ataques.Ataque import Ataque;
import random;

class PomadaWassington(Ataque):
    def __init__(self):
        self.damage = 5;
        self.addsHealth2attacker = True;
        self.extraDamage = 1;
    