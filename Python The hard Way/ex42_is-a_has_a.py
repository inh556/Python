## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## has-a name
        self.name = name

## is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## has-a name
        self.name = name

## person is-a object
class Person(object):

    def __init__(self, name):
        ## person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## is a 
        super(Employee, self).__init__(name)
        ## has-a salary 
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## is-a 
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass


## has-a
rover = Dog("Rover")

## has-a
satan = Cat("Satan")

## has-a
mary = Person("Mary")

## has-a
mary.pet = satan

## has-a
frank = Employee("Frank", 120000)

## has-a
frank.pet = rover

## has-a
flipper = Fish()

## has-a
crouse = Salmon()

## has-a
harry = Halibut()