class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Midpoint (0 = full, 10 = very hungry)
        self.energy = 5  # Midpoint (0 = tired, 10 = fully rested)
        self.happiness = 5  # Midpoint (0 = sad, 10 = very happy)
        self.tricks = []  # List to store learned tricks

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate food. Hunger: {old_hunger} -> {self.hunger}, Happiness increased to {self.happiness}.")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} slept well. Energy: {old_energy} -> {self.energy}.")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play.")
            return
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played! Energy now {self.energy}, Happiness now {self.happiness}, Hunger now {self.hunger}.")

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}! Happiness increased to {self.happiness}.")
        else:
            print(f"{self.name} already knows how to {trick}.")

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")


my_pet = Pet("Jsmummy")
my_pet.get_status()

my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.get_status()

my_pet.train("sit")
my_pet.train("roll over")
my_pet.train("sit")  # repeating the same trick
my_pet.show_tricks()
