import copy


class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.color} {self.make} {self.model}"

    def clone(self):
        return copy.deepcopy(self)


original_car = Car("Tesla", "Model S", "Red")
print("Original Car:", original_car)

cloned_car = original_car.clone()
print("Cloned Car:", cloned_car)
