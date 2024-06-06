from enum import Enum

class Difficulty(Enum):
    TRIVIAL = 1
    EASY = 2
    STANDARD = 3
    HARD = 4

class Encounter:
    def __init__(self, total=0, size=0, monsters={}):
        self.total = total
        self.size = size
        self.monsters = monsters

    def copy(self):
        return Encounter(self.total, self.size, self.monsters.copy())

    def add_monster(self, m):
        self.monsters[m] = self.monsters.get(m, 0) + 1
        self.total += m.cr
        self.size += 1

    def is_incomplete(self, budget, max_size):
        return self.total < budget and self.size < max_size

    def is_valid(self, budget, max_size):
        return self.total == budget and self.size <= max_size
    
    def has_leader(self):
        return any(m.role == "Leader" for m in self.monsters)

    def print(self):
        print(", ". join(f"{n} {m.name}" for m, n in self.monsters.items()))