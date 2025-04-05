class Superhero:
    # Defines a base class named 'Superhero' to represent a generic superhero
    def __init__(self, name, strength, speed):
        # Constructor method to initialize a Superhero object with specific attributes
        self._name = name          # Protected attribute storing the superhero's name (string)
        self._strength = strength  # Protected attribute for power level (1-100, integer)
        self._speed = speed       # Protected attribute for speed in km/h (integer/float)
        self._energy = 100        # Protected attribute starting at 100, representing energy level

    def use_power(self):
        # Method to simulate using a superpower, consuming energy
        if self._energy >= 20:    # Checks if energy is sufficient (at least 20)
            self._energy -= 20    # Reduces energy by 20 if condition is met
            return f"{self._name} unleashes their power! Energy remaining: {self._energy}"
            # Returns a string confirming power use and current energy
        return f"{self._name} is too exhausted to use powers!"
        # Returns a string if energy is too low

    def rest(self):
        # Method to restore energy when the superhero rests
        self._energy = min(100, self._energy + 30)
        # Increases energy by 30, but caps it at 100 using min()
        return f"{self._name} rests. Energy restored to {self._energy}"
        # Returns a string confirming rest and new energy level

    def get_stats(self):
        # Method to display the superhero's basic stats
        return f"Name: {self._name}\nStrength: {self._strength}\nSpeed: {self._speed}"
        # Returns a formatted string with name, strength, and speed

# Inherited class with specialized abilities
class FlyingSuperhero(Superhero):
    # Defines a subclass 'FlyingSuperhero' that inherits from 'Superhero'
    def __init__(self, name, strength, speed, flight_altitude):
        # Constructor for FlyingSuperhero, extending the parent constructor
        super().__init__(name, strength, speed)
        # Calls the parent class's __init__ to set name, strength, speed, and energy
        self.flight_altitude = flight_altitude  # Public attribute for max altitude (meters)

    def fly(self):
        # Method specific to flying superheroes, simulating flight
        if self._energy >= 30:    # Checks if energy is at least 30
            self._energy -= 30    # Reduces energy by 30 if condition is met
            return f"{self._name} soars to {self.flight_altitude} meters!"
            # Returns a string confirming flight and altitude
        return f"{self._name} is too tired to fly!"
        # Returns a string if energy is insufficient

    def get_stats(self):
        # Overrides the parent’s get_stats() method to include flight ability
        return f"{super().get_stats()}\nFlight Altitude: {self.flight_altitude}m"
        # Calls parent’s get_stats() and appends flight altitude

# Test the classes
hero1 = Superhero("Thunderbolt", 85, 120)
# Creates an instance of Superhero with name "Thunderbolt", strength 85, speed 120
hero2 = FlyingSuperhero("Sky Captain", 70, 300, 10000)
# Creates an instance of FlyingSuperhero with name "Sky Captain", strength 70, speed 300, altitude 10000

print(hero1.get_stats())
# Prints Thunderbolt’s stats: name, strength, and speed
print(hero1.use_power())
# Thunderbolt uses power, reducing energy from 100 to 80, and prints the result
print(hero1.rest())
# Thunderbolt rests, restoring energy (e.g., back to 100), and prints the result
print("\n")
# Prints a blank line for readability
print(hero2.get_stats())
# Prints Sky Captain’s stats, including flight altitude
print(hero2.fly())
# Sky Captain flies, reducing energy from 100 to 70, and prints the result
print(hero2.use_power())
# Sky Captain uses power, reducing energy from 70 to 50, and prints the result


class Vehicle:
    # Defines a base class 'Vehicle' to represent any vehicle type
    def __init__(self, name, max_speed):
        # Constructor to initialize a Vehicle object
        self.name = name          # Public attribute storing the vehicle’s name (string)
        self.max_speed = max_speed  # Public attribute for maximum speed (integer/float)

    def move(self):
        # Defines a base method 'move()' intended to be overridden by subclasses
        pass  # Empty implementation (placeholder) since it’s meant to be polymorphic

    def get_info(self):
        # Method to display basic vehicle information
        return f"Vehicle: {self.name}\nMax Speed: {self.max_speed}"
        # Returns a formatted string with name and max speed

class Car(Vehicle):
    # Defines a subclass 'Car' that inherits from 'Vehicle'
    def move(self):
        # Overrides the move() method to describe car-specific movement
        return f" {self.name} is driving at {self.max_speed} km/h!"
        # Returns a string indicating the car is driving with its max speed

class Plane(Vehicle):
    # Defines a subclass 'Plane' that inherits from 'Vehicle'
    def move(self):
        # Overrides the move() method for plane-specific movement
        return f" {self.name} is flying at {self.max_speed} km/h!"
        # Returns a string indicating the plane is flying with its max speed

class Boat(Vehicle):
    # Defines a subclass 'Boat' that inherits from 'Vehicle'
    def move(self):
        # Overrides the move() method for boat-specific movement
        return f" {self.name} is sailing at {self.max_speed} knots!"
        # Returns a string indicating the boat is sailing with its max speed

# Test polymorphism
vehicles = [
    Car("Speedster", 240),    # Creates a Car instance with name "Speedster", speed 240
    Plane("Jetstream", 900),  # Creates a Plane instance with name "Jetstream", speed 900
    Boat("Wave Rider", 45)    # Creates a Boat instance with name "Wave Rider", speed 45
]
# Stores all vehicle instances in a list to demonstrate polymorphism

for vehicle in vehicles:
    # Loops through each vehicle in the list
    print(vehicle.get_info())
    # Prints the vehicle’s name and max speed using the inherited get_info() method
    print(vehicle.move())
    # Calls the overridden move() method, showing different behavior for each subclass
    print()
    # Prints a blank line for readability between vehicles