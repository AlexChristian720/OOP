# a class data is the data that is shared among all the instances

#s InstanceCounter(object):
#count=0#class attr, will be accesible to all instances

#def __init__(self,val):
#    self.val=val
#    InstanceCounter.count+=1 #Increment the value of the class attr,accesible through class name.

#Above line,class('InstanceCounter') act as an object
#def set_val(self,newval):
#    self.val=newval

#def get_val(self):
#    return self.val

#def get_count(self):
#    return  InstanceCounter.count

#stanceCounter(9)
#stanceCounter(18)
#stanceCounter(27)

#obj in (a,b,c):
#print('val of obj: %s'%(obj.get_val()))#Initiliaze value

#print('count: %s'%(obj.get_count()))#always 3


class MyClass():
    class_attr=99

    def class_method(self):
        self.instance_attr='I am Instance Attr'
print(MyClass.__dict__)