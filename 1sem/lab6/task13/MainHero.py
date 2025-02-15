from lab6.task13.BaseCharacter import BaseCharacter


class MainHero(BaseCharacter):
    def __init__(self, x, y, hp):
        super().__init__(x, y, hp)
        self.weapon = None

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self} экипировал оружие: {weapon.name}.")

    def attack(self, target):
        if self.weapon is None:
            print("Герой не вооружён!")
            return False
        if not isinstance(target, BaseCharacter):
            print("Цель должна быть экземпляром BaseCharacter!")
            return False
        if not self.weapon.hit(self, target):
            print("Атака не удалась.")
        else:
            print(f"Герой успешно атаковал {target} с помощью {self.weapon.name}!")

    def next_weapon(self):
        if self.weapon is None:
            print("Герой не имеет оружия для переключения.")
        else:
            print(f"Герой больше не использует {self.weapon.name}. Теперь вооружён другим оружием.")

    def __str__(self):
        return f"MainHero(x={self.x}, y={self.y}, hp={self.hp})"
