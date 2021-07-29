# Converting bytes to text is called decoding

x = 'Tutorials Point'
# Initialised String

y=(b'Tutorials Point')

z=y.decode('ASCII')

if (z==x):
    print('Decoding Successful')
else:
    print('Decoding Unsucessful')



