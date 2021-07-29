from NegativeNumberException import NegativeNumberException
def enterage(age):
    if age<0:
        raise NegativeNumberException('Only Positive integers are allowed')

    if age %2 ==0:
        print('Entered age is even')

    else:
        print('Age is oddd')

try:
    num=int(input('Please Enter your Age: '))
    enterage(num)
except NegativeNumberException:
    print('only Positive integers are allowed')
except:
    print('Something is wrong!')

    