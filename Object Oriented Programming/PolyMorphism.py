#ss Animal(object):
# def __init__(self,name):
#     self.name=name
# def eat(self,food): # Common Method (Or Property) of both subclass
#     print('{0} eats {1}'.format(self.name,food))

#ss Dog(Animal):
# def fetch(self,thing):
#     print('{0} goes after the {1}'.format(self.name,thing))

# def show_affection(self): # Sam Method is caleed in the dog class
#     print('{0} wags tail '.format(self.name))

#ss Cat(Animal):
# def substring(self):
#     print('{0} shreds the string!'.format(self.name))

# def show_affection(self): # same method is called in Cat Class
#     print('{0} purrs'.format(self.name))


# a in Dog('Rover'),Cat('Fluffy'),Cat('Perfection'),Dog('Scrout'):
#      a.show_affection()
#


x=dir(len('hello'))

print(x)
y=dir(len([1,2,3]))
print(y)

z=dir(len({'a':9}))
print(z)

