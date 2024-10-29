# base class
class Animal:
    def __init__(self, name, habitat, sound):
        self._name = name         # Encapsulated attribute
        self._habitat = habitat   # Encapsulated attribute
        self._sound = sound       # Encapsulated attribute


    # getter methods
    def get_name(self):
        return self._name


    def get_habitat(self):
        return self._habitat


    # method outputs animal sound
    def speak(self):
        return f"{self._name} makes a sound: {self._sound}"



# dog subclass inherits from animal class
class Dog(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, habitat, "woof??")  # dog-specific sound


    # Overriding the speak method to show polymorphism
    def speak(self):
        return f"{self.get_name()} says {self._sound} in {self.get_habitat()}"


    # unique dog behavior
    def fetch(self):
        return f"{self.get_name()} is fetching the ball"


# cat subclass inherits from animal class
class Cat(Animal):
    def __init__(self, name, habitat):
        super().__init__(name, habitat, "mew")  # cat-specific sound


    # Overriding the speak method to show polymorphism
    def speak(self):
        return f"{self.get_name()} says {self._sound} in {self.get_habitat()}"


    # unique cat behavior
    def climb(self):
        return f"{self.get_name()} is climbing a tree"


# testing the classes
def main():
    # Create Dog and Cat objects
    bub = Dog("bub", "the backyard")
    mipy = Cat("mipy", "the living room")


    # Call the speak method on each object
    print(bub.speak())       # demonstrates polymorphism
    print(bub.fetch())       # dog-specific behavior


    print(mipy.speak())    # demonstrates polymorphism
    print(mipy.climb())    # cat-specific behavior


# Run the main function
if __name__ == "__main__":
    main()