class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)
    def __eq__(self):
        return self.numberOfFloors == self.buildingType

h1 = Building(10, 'barn')
print(h1.__eq__())