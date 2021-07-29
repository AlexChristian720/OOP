# Simple Method
#Outside of a class
def outside_func():
    pass

#Instance Method

def func(self,):
    pass

#if we need to use class attr
class C(object):
    @classmethod
    def fun(cls,arg1,arg2):
        pass

#Do Not Have Any info about the class
class C1(object):
    @staticmethod
    def fun(arg1,arg2):
        pass
