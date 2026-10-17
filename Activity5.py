class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def start(self):
        print("Car engine is starting.")

if __name__ == "__main__":
    general_vehicle = Vehicle("Generic", 0)
    my_car = Car("Toyota", 0)

    general_vehicle.start()
    my_car.start()