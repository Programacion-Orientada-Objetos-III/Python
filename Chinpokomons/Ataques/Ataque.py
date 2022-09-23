class Ataque:
    def __init__(self):
        self.damage = None;
        self.addsHealth2attacker = None;
        self.extraDamage = None;
    #Property getters    
    @property
    def damage(self):
        return self.__damage;
    @property
    def addsHealth2attacker(self):
        return self.__addsHealth2attacker;
    @property 
    def extraDamage(self):
        return self.__extraDamage;
    #Property setters
    @damage.setter
    def damage(self,damage):
        self.__damage = damage;
    @addsHealth2attacker.setter
    def addsHealth2attacker(self,addsHealth2attacker):
        self.__addsHealth2attacker = addsHealth2attacker;    
    @addsHealth2attacker.setter
    def extraDamage(self,extraDamage):
        self.__extraDamage = extraDamage;    
    
    #Methods

    def realizarAtaque(self,chinpokomonAtacante,chinpokomonDefensor):
        extraDamageToAtack = 0;
        if(chinpokomonAtacante.tieneVentajaContra(chinpokomonDefensor)):
            extraDamageToAtack = self.extraDamage;
        damageToAtack = self.damage + extraDamageToAtack;
        if(self.addsHealth2attacker):
            chinpokomonAtacante.addLife(damageToAtack);
        else:
           chinpokomonDefensor.dealDamage(damageToAtack);
        