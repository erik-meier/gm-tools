class Monster():
    def __init__(self, name, cr, role):
        self.name = name
        self.cr = cr
        self.role = role

    def __lt__(self, other):
        return self.cr < other.cr
    
    def print(self):
        print(self.name, end="")