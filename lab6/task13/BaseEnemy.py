from lab6.task13.BaseCharacter import BaseCharacter


class BaseEnemy(BaseCharacter):
    def __init__(self, x, y, hp, name):
        super().__init__(x, y, hp)
        self.name = name

    def __str__(self):
        return self.name

    def hit(self, target):
        print(f"{self.name} не имеет оружия по умолчанию.")
