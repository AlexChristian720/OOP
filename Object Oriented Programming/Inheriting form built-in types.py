class MyList(list):
    def __getitem__(self, item):
        if item ==0 :
            raise IndexError


        if item > 0:
            item=item -1
            return list.__getitem__(self,item) #This is ,method is called when we access a value with subscript like x[1]
    def __setitem__(self, key, value):
        if key == 0:
            raise IndexError
        if key >0:
            list.__setitem__(self,key,value)

X=MyList(['a','b','c']) #__init__() inherited from built-in list
print(X) # __repr__() inherited from built-in list

X.append('Hello') # Append() inherited from built-in list

print(X[1])
print(X[4])





