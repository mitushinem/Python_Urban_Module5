class Buiding():
    def __init__(self, numberOfFloors, buildingType='multi-storey building'):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType:
            return 'Объекты равны'
        else:
            return 'Объекты не равны'


a = Buiding(3)
b = Buiding(3, 'building')
print(a == b)
