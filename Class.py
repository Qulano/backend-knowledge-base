import random
from abc import ABC, abstractmethod
class Unit(ABC):
    @abstractmethod
    def attack(self):
        pass
    
    def take_damage(self):
        pass
    
    def __str__(self):
        return f"{self.name} ({self.hp} HP)"
    
    def __bool__(self):
        return self.hp > 0
    
    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Unit):
            return False
        return self.name == other.name and self.hp == other.hp
    
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
    
    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Здоровье должно быть числом")
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value
        
     

class Orc(Unit):
   
    def attack(self, target):
            damage = random.randint(15,20)
            print(f"Орк {self.name} рубит {target} на {damage} урона!")
            target.take_damage(damage)
        
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} получил урон, осталось {self.hp} HP")
        
    
    def __repr__(self):
        return f"Orc(name={self.name}, hp={self.hp})"
        
class Archer(Unit):
    
    def attack(self, target):
        damage = random.randint(15,20)
        print(f"Лучник {self.name} стреляет в {target} на {damage} урона!")
        target.take_damage(damage)
        
    def take_damage(self, damage):
            self.hp -= damage
            print(f"{self.name} получил урон, осталось {self.hp} HP")
        
        
orc = Orc("Thrall", 120)
orc2 = Orc("Thrall", 120)
print(orc == orc2)
print(orc.hp)

orc.hp = 70
print(orc.hp)

    
    