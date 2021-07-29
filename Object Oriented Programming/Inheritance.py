#Inheritance means to re-use
#The Inheritance prvides a way to organize code, rather than rewrting it from scratch

class BaseClass:
    pass
    #Body of Base Class
class DerivedClass(BaseClass):
    pass
#Body of the dervied class

class Date(object):#Inherits from the 'object 'class
    def get_date(self):
        return '14-April-2021'

class Time(Date):#Inherits from the 'Date'Class
    def get_time(self):
        return '12:41:00'

dt=Date()
print('Get date from the date class: ',dt.get_date())
tm=Time()
print('Get time from the Time Class: ',tm.get_time())
print('Get date from the clas by inheriting or calling date class method',tm.get_date())#Found this method in the date class

