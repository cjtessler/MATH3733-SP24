class Car:
    """A simple attempt to model a var."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.wheels = 4
        self.gas_tank = 100

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"
    
    def get_odometer(self):
        return self.odometer_reading
    
    def set_odometer(self, miles):
        """Set the odometer reading to a given value.
        Reject the change if it attempts to roll back the odometer."""
        if self.odometer_reading >= miles:
            print("We can roll back the odometer!")
        else:
            self.odometer_reading = miles

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def describe_wheels(self):
        print(f"This car has {self.wheels} wheels.")

    def get_gas_tank(self):
        print(f"The gas tank is at {self.gas_tank}%.")


class ElectricCar(Car):
    """Represents aspects of a car, specific  to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of your parent class."""
        super().__init__(make, model, year)
        self.battery_size = 60

    def describe_battery(self):
        """Print battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_gas_tank(self):
        print("This car does not have a gas tank.")

class Motorcycle(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year) 
        self.wheels = 2

    def describe_wheels(self):
        print(f"This bike has {self.wheels} wheels.")

my_tesla = ElectricCar('tesla', 'model y', 2024)
print(my_tesla)
my_tesla.get_gas_tank()

my_bike = Motorcycle("Harley Davidson", "Road Glide", 2024)
print(my_bike)
my_bike.describe_wheels()