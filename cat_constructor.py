from animal_parent_class import Animal

class Cat(Animal):

    def __init__(self, animal_name, breed="", colour="", hunger_bar="full", tiredness="awake", age=0):
        self.breed = breed
        self.colour = colour
        self.hunger_bar = hunger_bar
        self.tiredness = tiredness
        self.__age = int(age)
        self.name = animal_name
        super().__init__(4,"0.3m","5kg")

    def meow(self):
        self.tiredness = "tired"
        return "Meow!"

    def yawn(self):
        return "Reowwww, So tired!!!"

    # Getter method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, new_age):
        self.__age = new_age

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