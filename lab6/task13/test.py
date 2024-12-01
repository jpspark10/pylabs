# Создание оружия
from lab6.task13.BaseEnemy import BaseEnemy
from lab6.task13.MainHero import MainHero
from lab6.task13.Weapon import Weapon

if __name__ == "__main__":
    sword = Weapon("Меч", 50, 1)
    bow = Weapon("Лук", 30, 5)

    hero = MainHero(0, 0, 200)
    enemy = BaseEnemy(3, 4, 100, "Гоблин")

    hero.equip_weapon(sword)

    hero.attack(enemy)

    hero.equip_weapon(bow)
    hero.attack(enemy)

    hero.move(2, 3)
    print(hero.get_coords())
