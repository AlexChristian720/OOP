# converting text to bytes is called encoding
# Python Code to demonstrate string encoding

# Initialising a string

x='TutorialsPoint'

#Initialising a byte object
y=b'Hello Alex'

#using encode() to encode the string

# encoded version of x is stored in z using ASCII mapping


z=x.encode('ASCII')
# Check if x is converted to bytes or not!
if (z == y):
    print('Encoding succesful')
else:
    print("So, Sorry we can't make it happen ")
