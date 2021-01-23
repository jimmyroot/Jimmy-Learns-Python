class Animal:

    def __init__(self, species, weight_in_lbs, sound, colour):
        self.species = species
        self.weight = weight_in_lbs
        self.sound = sound
        self.colour = colour

    def eat(self, food):
        return f"A {self.species} eats some {food}."

    def sleep(self, time_in_minutes):
        return f"A {self.species} sleeps for {time_in_minutes} minutes."

    def walk(self):
        return f"A {self.species} mooches about for a bit."

    def vocalize(self):
        return f"A {self.species} says {self.sound}"

class Pig(Animal):

    def wallow(self, mood):
        return f"A {self.species} {mood} wallows in the mud."

    def snuffle(self):
        return f"A {(self.species).lower()} is snuffling for truffles."

class Chicken(Animal):
    def pecks(self, object):
        return f"A {(self.speciecs.lower())} pecks at some {object}"

    def lay_egg(self, colour):
        return f"A {(self.species).lower()} lays a {colour} egg."

class Cow(Animal):
    def graze(self):
        return f"A {self.species} grazes peacefully in the field"

    def stare(self, mood):
        return f"A {self.species} stares {mood}."

class Horse(Animal):
    def gallop(self):
        return f"A {self.species} gallops across the meadow."

    def groom(self):
        return f"A {self.species} is performing a little self care."
    
pig1 = Pig("Pig", 500, "oink", "pink")
chicken1 = Chicken("Chicken", 6, "cluck", "white")
cow1 = Cow("Cow", 2000, "Moo", "brown")
horse1 = Horse("Horse", 2500, "neigh", "black")

