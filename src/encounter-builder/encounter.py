class Encounter:
    def __init__(self, total=0, monsters={}):
        self.total = total
        self.monsters = monsters

    def copy(self):
        return Encounter(self.total, self.monsters.copy())

    def add_monster(self, m, cr):
        self.monsters[m] = self.monsters.get(m, 0) + 1
        self.total += cr

    def freeze(self):
        return frozenset(self.monsters)

    def print(self):
        print(", ". join(f"{n} {m}" for m, n in self.monsters.items()))