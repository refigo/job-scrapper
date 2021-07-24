def plus(*args):
    result = 0
    for number in args:
        result += number
    print(result)

#plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

class Car():
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def start(self):
        print(self.doors)
        print("I started")
    
    def __str__(self):
        return f"Car with {self.wheels} wheels"

class Convertible(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return "Car with no roof"

#porche = Car(color="green", price="$40")
#porche.color = "Red"
#porche.start()
#print(porche) # proche.__str__()
#print(porche.color, porche.price)

mini = Car()
print(mini.color, mini.price)

porche = Convertible(color="green", price="$40")
print(porche.take_off())
print(porche)
print(porche.color)
