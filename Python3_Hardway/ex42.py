## Animal is-a object

class Animal(object):
    pass

## is a
class Dog(Animal):

    def __init__(self, name):
        ## has a
        self.name = name

## is a
class Cat(Animal):

    def __init__(self, name):
        ## has a
        self.name = name

## is a
class Person(object):

    def __init__(self, name):
        ## has a
        self.name = name
        ## Person has a pet of some kind
        self.pet = None

## is a
class Employee(Person):

    def __init__(self, name, salary):
        ## has a hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## has a
        self.salary = salary

## is a
class Fish(object):
    pass

## is a 
class Salmon(Fish):
    pass

## is a
class Halibut(Fish):
    pass


## rover is a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a Person
mary = Personal("Mary")

## has a
mary.pet = satan

## is a
frank = Employee("Frank", 120000)

## has a pet
frank.pet = rover

## is a
flipper = Fish()

## is a
crouse = Salmon()

## is a 
harry = Halibut()
