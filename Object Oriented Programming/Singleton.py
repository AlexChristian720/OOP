#Singleton Pattern

class Logger(object):
    def __new__(cls, *args, **kwargs): # Constructs a new instance
        if not hasattr(cls,'_logger'):
            cls._logger=super(Logger, cls).__new__(cls,*args,**kwargs)

        return cls._logger

obj1=Logger('Hello World!')
obj2=Logger()

print(obj1 == obj2)

print(obj1)
print(obj2)


