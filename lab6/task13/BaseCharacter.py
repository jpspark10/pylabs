class BaseCharacter:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp = max(self.hp - amount, 0)
        if self.hp == 0:
            print(f"{self} погиб.")

    def get_coords(self):
        return self.x, self.y
