class Buiding():
    total = 0

    def __init__(self, name):
        Buiding.total += 1


for i in range(40):
    new_buiding = Buiding(i)

print(Buiding.total)
