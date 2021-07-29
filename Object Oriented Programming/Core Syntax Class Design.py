class SumList(object):
    def __init__(self,myList):
        self.myList=myList

    def __add__(self, other):
        newList=[x+y for x,y in zip(self.myList,other.myList)]
        return SumList(newList)

    def __repr__(self):
        return str(self.myList)

aa=SumList([3,6,9,12,15])
bb=SumList([100,200,300,400,500])

cc=aa+ bb # aa.__add__(bb)

print(cc) # should gives us a list ([ 103, 206, 309 ,412,515])


