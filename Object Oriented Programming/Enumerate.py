#Enumarate

#Adds a counter to an iterable and returns the enumarate object

#The Syntax of the enumarate is
#enumerate(iterable,start=0)


names=['Rajesh','Rahul','Aarav','Sahil','trevor']
print(enumerate(names))

print(list(enumerate(names)))

for i , n in enumerate(names):
    print('Names Number: '+ str(i))
    print(n)

