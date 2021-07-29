class Myclass(object):
    def __init__(self,aaa,bbb):
        self.a=aaa
        self.b=bbb
        self.data=[]

    def setAge(self,num):
        self.age=num

    def getAge(self):
        return self.age

Zack=Myclass

print(Zack.getAge)


print(Zack.getAge)

x=Myclass(4.5,3)
print(x.a,x.b)




