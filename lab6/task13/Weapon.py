class Weapon:
    def __init__(self, name, damage, range_):
        self.name = name
        self.damage = damage
        self.range = range_

    def hit(self, actor, target):
        if actor.get_coords() == target.get_coords():
            print(f"{self.name} слишком близко к {target}. Аттаковать невозможно.")
            return False

        distance = ((actor.get_coords()[0] - target.get_coords()[0])**2 +
                    (actor.get_coords()[1] - target.get_coords()[1])**2) ** 0.5
        if distance <= self.range:
            target.get_damage(self.damage)
            return True
        else:
            print(f"{self.name} промазал по {target}. Не дотянулся.")
            return False
