class Animal(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):# Common method(or property) of both subclass
        print('%s is eating %s. '%(self.name,food))

class Dog(Animal):
    def fetch(self,thing):
        print('%s goes after the %s!'%(self.name,thing))

class Cat(Animal):
    def swatstring(self):
        print('%s shreds the string! '%(self.name))

D=Dog('Ranger') # Created Dog Object,d
C=Cat('MeOw') #Created Cat Object,C

print(D.fetch('ball')) #Rover goes after the paper
print(C.swatstring()) # fluufy shreds the string
print(D.eat('Dog Food')) # rover is eating the dog food
D.swatstring() #Error

