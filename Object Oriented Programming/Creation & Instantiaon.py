class MyClass(object):
    var=9
    def firstM(self):
        print('Hello World')
        print(self)

#Creating the first instance of the class

this_obj=MyClass()
print(this_obj.var)
print(this_obj.firstM())

#Another Instance of MyClass
that_obj=MyClass()
print(that_obj.var)
print(this_obj)

'''''when requested for an attribute 
from an instance, the instance looks for the attribute and the class. This is called the 
attribute lookup'''''

