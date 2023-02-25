class car:

    name= ""
    cylinder= 0
    color=""
    model=2000
    price=0

    def __init__(self,name,cylinder, color, model, price):
        print("new car")

        self.name=name
        self.cylinder=cylinder
        self.color=color
        self.model=model
        self.price=price

car_1=car("bmw",5,"yellow",2005,9000)
car_2=car("mercedes c200",6,"silver",2017,17000)

print(car_1.name)