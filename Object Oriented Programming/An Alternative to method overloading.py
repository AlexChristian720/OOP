class Human:
    def sayHello(self,name=None):
        if name is not None:
            print('Hello ',name)
        else:
            print('Hello')

#Creating Instance

obj=Human()

#Call The Method, else part will be executed
print(obj.sayHello())

#Call the method with a parameter,if part will be executed

obj.sayHello('Rahul')