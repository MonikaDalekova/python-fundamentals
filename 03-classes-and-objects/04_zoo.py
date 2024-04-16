class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammals":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)

        Zoo._Zoo__animals += 1   # тъй като е клас атрибут, ние достъпваме през името на класа.
                                 # Ако беше инстанс атрибут, достъпваме със self

    def get_info(self, species):
        info = ""
        if species == "mammals":
            info += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fishes":
            info += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "birds":
            info += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        info += f"Total animals: {Zoo._Zoo__animals}"
        return info


name = input()
rows = int(input())

zoo = Zoo(name)

for _ in range(0, rows):
    species, name = input().split()
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))