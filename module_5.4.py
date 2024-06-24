class Building:
    total = 0
    def __init__(self):
        Building.total += 1
        self.total = Building.total

for i in range(40):
    building = Building()
    print(building.total)
