class customException(Exception):
    def __init__(self,value):
        self.parameter=value

    def __str__(self):
        return repr(self.parameter)

try:
    raise customException('My Useful Error Message!')
except customException as instance:
    print('Caught: ' + instance.parameter)

        