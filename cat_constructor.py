class Cat:

    def __init__(self, breed="", colour="", hunger_bar="full", tiredness="awake", age=""):
        self.breed = breed
        self.colour = colour
        self.hunger_bar = hunger_bar
        self.tiredness = tiredness
        self.age = int(age)

    def meow(self):
        self.tiredness = "tired"
        return "Meow!"

    def eat(self):
        if self.hunger_bar.lower() == "full":
            return "I'm already full! MEOW."
        elif self.hunger_bar.lower() != "full":
            self.hunger_bar = "full"
            return "MMM.. Food.. YUM!"

    def sleep(self):
        if self.tiredness.lower() == "awake":
            return "Meow, im not tired enough to sleep"
        elif self.tiredness.lower() == "tired":
            self.tiredness = "awake"
            return "ZZzzZZzzZZzz"

    def purr(self):
        return "Purrrrrrrr"