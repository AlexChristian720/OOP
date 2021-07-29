#class A(object):
#    def dothis(self):
#        print('Doing this in A')
#
#class B(A):
#    pass
#
#class C(object):
#    def dothis(self):
#        print('do this in C')
#
#class D(B,C):
#    pass
#
#d_instance=D()
#d_instance.dothis()
#
#print(D.mro())

class A(object):
    def dothis(self):
        print('Doin This In A')
class B(A):
    pass

class C(A):
    def dothis(self):
        print('Do this in C')

class D(B,C):
    pass

d_instance=D()
d_instance.dothis()

print(D.mro())

#If the Same Class Appear In the Method Resolution Order(M.R.O), the earlier apperances of this case will be removed from the method resolution order

