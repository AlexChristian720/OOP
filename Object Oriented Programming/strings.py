# String example
a='hello'
b= '''A Multi Line String,
Simple!'''
e=('Multiple''Strings''together')
#print('This is a obj and it is',a.isdigit())
#print('This is a obj and it is',a.isalpha())
#print('This is a obj and it is',a.isdecimal())
#print('This is a obj and it is',a.isnumeric())
#print('This is a obj and it finds',a.find('h'))
#print('This is a obj and it is',a.istitle())
#print('This is a obj and it is',a.join(a))
##print('This is a obj and it is',a.bytearray())
#print('This is a obj and it is',a.partition('a'))
#print('This is a obj and it is',a.encode())
#print('This is a obj and it is',a.isprintable())


#str1= 'Hello World!'
#print(str1.startswith('H'))
#print(str1.startswith('h'))
#print(str1.endswith('d'))
#print(str1.endswith('D'))
#print(str1.endswith('d!'))

#name=str(input('Please enter your name: '))
#print('Hello {}'.format(name))
#number_and_name=int(input('Please Enter any 10 digit random number: ' ))
#print('So the number you have chosen was {} {}!.'.format(number_and_name,name))
#print('{1} {0}'.format('pie','3.149249434'))


#print('{:12}'.format('PYTHON'))
#print('{:>12}'.format('PYTHON'))
#print('{:<{}s}'.format('PYTHON',12))
#print('{:*<12}'.format('PYTHON'))
#print('{:*^12}'.format('PYTHON'))
#print('{:.15}'.format('PYTHON OBJECT ORIENTED PROGRAMMING'))#Truncated 15 characters from the left side of a special string
#print('{:.{}}'.format('PYTHON OBJECT ORIENTED',15))

# Named Placeholder
data={'Name':'Raghu','Place':'Banglore'}
print('{Name} {Place}'.format(**data))

# Date Time

from datetime import datetime
print('{:%Y/ %m/ %d.%H:%M}'.format(datetime(2021,4,23,13,27)))
