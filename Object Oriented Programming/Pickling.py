import Unpickling
import pickle

class Animal:
    def __init__(self,number_of_legs,color):
        self.number_of_legs=number_of_legs
        self.color=color

class Cat(Animal):
    def __init__(self,color):
        Animal.__init__(self,4,color)

pussuy=Cat("White")
print(str.format('My Cat Pussy is {0} and has {1} legs', pussuy.color,pussuy.number_of_legs))
pickled_pussy=pickle.dumps(pussuy)#Serializes a string!
print("Would you like to see her pickled? Here she is!")
print(pickled_pussy)

binary_file=open('my_pickled_Pussy.bin',mode='wb')
#my_pickled_Pussy=pickle.dumps(pussuy,binary_file)
binary_file.close()
