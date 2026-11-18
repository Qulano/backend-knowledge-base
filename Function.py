import time
import random
from functools import wraps

#First-class citizen
def hit():
    return "удар топором"

def regen():
    return "лечение зельем"

abil = {
    1: hit,
    2: regen
    }

def cast(ability):
    return f"Кастую {ability()}"

print(cast(abil[random.randint(1,2)]))



def battle_cry(race):
    def cry():
        return "AAAAAAA"
    def rgh():
        return "Ргххххх"
    race_battle_cry = {
        "human": cry,
        "orc": rgh
    }
    return race_battle_cry.get(race)
        
c = battle_cry("orc")
print(c())


#Positional and Keyword arguments, Arguments Packing Unpacking
def funct(hero_name, *item, **stats):
    print(hero_name)
    print(item, type(item))
    print(stats, type(stats))
    
funct("Grog", "меч", "зелье", gold=50, mana=100)
bag = ["посох", "лук", "колчан"]
bonus = {
    "armor": 50
}

funct("Grog", *bag, **bonus)

#Замыкания Closures и nonlocal
def create_attack(weapon, damage):
    uses = 0
    def attack(target):
        nonlocal uses
        uses += 1
        print(f"Удар {uses} Цель {target} получила {damage} урона с помощью {weapon}")
    return attack

axe_hit = create_attack("Топор", 40)
bow_hit = create_attack("Лук", 25)
axe_hit("Гоблин")
axe_hit("Гоблин")
bow_hit("Тролль")

def battle_cry(cry):
    def character(unit):
        print(f"Игровой юнит {unit} издал боевой клич {cry}")
    return character

human_cry = battle_cry("АААААААА")
human_cry("Человек")


#Декораторы
def cache(func):
    result_dict = {}
    @wraps(func)
    def wrapper(*argv, **kwargs):
        if argv in result_dict:
            print(f"Результат прилетел из кэша")
            return result_dict[argv]
        else:
            print(f"Отработала функция: {func.__name__} результат, сохранен в кэш")
            result = func(*argv, **kwargs)
            result_dict[argv] = result
            return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*argv, **kwargs):
        start = time.perf_counter()
        result = func(*argv, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"Отработала функция: {func.__name__} за {duration:.9f} секунд")
        return result
    return wrapper

@timer
@cache
def summer(n: int):
    result = sum(range(n))
    return result

print(summer(100_000_000))
print(summer(100_000_000))
print(summer.__name__)


#ООП со звездочкой
class WeaponAttck:
    def __init__(self, weapon: str, damage: int):
        self.weapon = weapon
        self.damage = damage
        self.uses = 0
        
    def __call__(self, target: str):
        self.uses += 1
        return f"Удар {self.uses} Цель {target} получила {self.damage} урона с помощью {self.weapon}"
    
    @classmethod
    def from_string(cls, data: str):
        weapon, damage = data.split(":")
        return cls(weapon, int(damage))
    
    @staticmethod
    def is_critical(damage: int):
        return damage >= 50
        
#Работа dunder метода __call__ который позволяет использовать объект класса непосредственно как функцию    
axehit = WeaponAttck("Топор", 40)
print(axehit("Гоблин"))
print(axehit("Гоблин"))
print(axehit.uses)

#Декораторы @classmethod и @staticmethod
bow_hit = WeaponAttck.from_string("Лук: 75")
print(bow_hit("Тролль"))
print(WeaponAttck.is_critical(25))
print(WeaponAttck.is_critical(82))

#Транзитный проброс
class FireWeapon(WeaponAttck):
    def __init__(self, *args, fire_damage: int = 15, **kwargs):
        super().__init__(*args, **kwargs)
        self.fire_damage = fire_damage
    def __call__(self, target: str):
        base_mg = super().__call__(target)
        return f"{base_mg} + {self.fire_damage} урона огнем"
    
fire_sword = FireWeapon("Огненный меч", 50, fire_damage=25)
print(fire_sword("Дракон"))
        
#Контекстные менеджеры в пайтон
class DataBaseTransaction:
    def __enter__(self):
        print("🔓 BEGIN: Открываю транзакцию БД...")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"💥 Ошибка ({exc_val})! Делаю ROLLBACK транзакции!")
            return False
        else:
            print("✅ Всё чисто! Делаю COMMIT транзакции!")
            
with DataBaseTransaction():
    print(" Записываю нового пользователя в таблицу...")

try:
    with DataBaseTransaction():
        print(" Пытаюсь списать баланс...")
        1 / 0
except ZeroDivisionError:
    print("Поймали ошибку")

