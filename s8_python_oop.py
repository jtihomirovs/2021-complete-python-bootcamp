# For class we follow CamelCasing
# For variable names and function names we follow snake_casing

# define class
class Sample():
    pass


# create an instance of class
my_sample = Sample()

# check type
print(type(my_sample))

'''
class Dog():
    # self connects this method to instance of class
    def __init__(self, mybreed):
        # We take in the argument
        # Assign it to the instance using self.attribute_name
        self.my_attribute = mybreed
        
my_dog = Dog(mybreed='Lab')

my_dog.my_attribute
'''


# define dog class
class Dog():
    # class object atributes
    # same for any instance of a class
    species = 'Mammal'

    # self connects this method to instance of class
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        # Expect boolean True/False
        self.spots = spots

    # operations / Actions --> Methods (basically loook lika functions inside class)
    # Method is a function that is inside class
    # Function is outside a class

    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))
        print(f"WOOF! My name is {self.name} and the number is {number}")


# my_dog = Dog(breed='Lab',name='Sammy',spots=False)


my_dog = Dog('Lab', 'Sammy', False)

print(type(my_dog))

print(my_dog.breed, my_dog.name, my_dog.spots, my_dog.species)

my_dog.bark('22')


class Circle():
    # Class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        # we can caculate an area
        # instead of self.pi we can write Circle.pi
        self.area = radius * radius * self.pi

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2


# example with the use of default value
my_circle = Circle()
print('Circle 1 area: ', my_circle.area)
print('Circle 1 circumference: ', my_circle.get_circumference())

my_circle = Circle(22)
print('Circle 2 area: ', my_circle.area)
print('Circle 2 circumference: ', my_circle.get_circumference())


# Inheritance and Polymorphism
# Create base class
class Animal():
    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am animal')

    def eat(self):
        print('I am eating')


# derived class - Cat()
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cat Created')

    # we can overwrite method
    def who_am_i(self):
        print('I am a cat')


my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

my_cat = Cat()
my_cat.who_am_i()
my_cat.eat()


# Polymorphism
class Mouse():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says pii!"


class Hamster():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says puff!"


niko = Mouse('Niko')
felix = Hamster('Felix')

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


class AnimalBase():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


my_animal = AnimalBase('Ted')


# my_animal.speak()


class Rabbit(AnimalBase):
    def speak(self):
        return self.name + 'says woop!'


class Bunny(AnimalBase):
    def speak(self):
        return self.name + 'says woopwoop!'


robert = Rabbit('Robert')
rodger = Bunny('Rodger')

print(robert.speak())
print(rodger.speak())


# Real life examples with polymorphism - base class for opening failes (method - open) and subclasses for pdf open,
# xls open and other... share the same method name

# Special (Magic/Dunder) methods
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')


b = Book('Python rocks', 'Jose', 200)

print(b)

print(str(b))

print(len(b))

del b
