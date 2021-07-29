import pickle
class Animal:
    def __init__(self,number_of_legs,colors):
        self.number_of_legs=number_of_legs
        self.color=colors

class Cat(Animal):
    def __init__(self,color):
        Animal.__init__(self,4,color)



# Step-1: Let's create the cat pussy

pussy=Cat("White")

#Step 2: Let's Pickle Pussy!

my_pickled_pussy=pickle.dumps(pussy)

#Step:3 Let's unpickle our cat Pussy creating another instance, another cat

MeOw=pickle.loads(my_pickled_pussy)

# MeOw and Pussy are two different objects, in fact we specify another color for MeOw
# There are no Consequences for Pussy

MeOw.color="Black"
print(str.format("MeOw is {0} ",MeOw.color))
print(str.format("Pussy is {0} ", pussy.color))


