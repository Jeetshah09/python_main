# Superclass 1: Ferrari
class Ferrari:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def display_ferrari(self):
        print(f"Ferrari Model: {self.model}, Speed: {self.speed} km/h")

# Superclass 2: Benz
class Benz:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display_benz(self):
        print(f"Benz Model: {self.model}, Color: {self.color}")

# Subclass: Car (inherits from Ferrari and Benz)
class Car(Ferrari, Benz):
    def __init__(self, ferrari_model, ferrari_speed, benz_model, benz_color):
        # Initialize both Ferrari and Benz constructors
        Ferrari.__init__(self, ferrari_model, ferrari_speed)
        Benz.__init__(self, benz_model, benz_color)

    def display_car(self):
        # Call methods from both Ferrari and Benz
        self.display_ferrari()
        self.display_benz()

# Example usage:
car = Car("Ferrari F8", 340, "Benz S-Class", "Black")
car.display_car()
