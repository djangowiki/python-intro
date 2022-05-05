# Classes are a form of objects that has certain properties or attributes.
# Classes have their own variables, descriptions and functions (known as methods)
# A class is something a developer can create. Just like lists and tuples are all classes created in python
# A classes when we write functions, we always have to put self.
# If we want to access the properties of the class, we always use the self keyword.

# How to create a class:
# class PythonClass:
#     def __init__(self): #this function initializes the class and its attributes
#         self.Attribute = 0

#     def AnotherFunction(self):
#         Codes;


# class Team:
#     def __init__(self):
#         self.TeamName = "Jordan"
#         self.TeamOrigin = "Anambra"


# Team1 = Team()
# print(Team1.TeamName)
# print(Team1.TeamOrigin)


class Pet:
    def __init__(self, name, age, hunger, playful):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.playful = playful

    # getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful

    # setters
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setHunger(self, age):
        self.age = age

    def setPlayful(self, playful):
        self.playful = playful

    def __str__(self):
        return f"{self.name} is {self.age} years old"


Pet1 = Pet("Bingo", 3, False, True)
# print(Pet1.name)
# print(Pet1.age)
# print(Pet1.getName())
# Pet1.setName("Danco")
# print(Pet1.name)
# print(Pet1.getName())


class Dog(Pet):
    def __init__(self, name, age, hunger, playful, breed, favoriteToy):
        Pet.__init__(self, name, age, hunger, playful)
        self.breed = breed
        self.favoriteToy = favoriteToy

    def wantsToPlay(self):
        if self.playful == True:
            return f"{self.name} wants to play with {self.favoriteToy}"
        else:
            return "Dog does not want to play"

    # Default Overrider
    def __str__(self):
        return f"The dog name is {self.name} from {self.breed} breed and it is {self.age} years old."


class Cat(Pet):
    def __init__(self, name, age, hunger, playful, place):
        Pet.__init__(self, name, age, hunger, playful)
        self.favoritePlace = place

    def wantsToSit(self):
        if self.playful == False:
            print(f"{self.name} wants to sit on {self.favoritePlace}")
        else:
            print(f"{self.name} wants to play")

    def __str__(self):
        return f"{self.name} is {self.age} years old and likes to sit on {self.favoritePlace}"


class Human:
    def __init__(self, name, pets):
        self.name = name
        self.pets = pets

    def hasPets(self):
        if len(self.pets) != 0:
            return f"{self.name} has pets"
        else:
            return f"{self.name} does not have pets"

    def showPets(self):
        for pet in range(len(self.pets)):
            return pet

    def __str__(self):
        return f"{self.name} has pet"


germanShepherd = Dog("Danco", 4, False, True, "german shepherd", "bone")

print(germanShepherd.wantsToPlay())
print(germanShepherd)
germanShepherd.playful = False
print(germanShepherd.wantsToPlay())

typicalCat = Cat("Eve", 5, True, False, "Garrage")
typicalCat.wantsToSit()
print(typicalCat)
print(Pet1)

averageHuman = Human("Geby", [germanShepherd, typicalCat])
hasPet = averageHuman.hasPets()
showPet = averageHuman.showPets()

print(hasPet)
# print(showPet)
print(averageHuman.pets[1])
