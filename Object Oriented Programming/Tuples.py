stock=('MSFT',95.00,97.45,92.45,)
stock2=('MSFT',95.00,97.45,92.45,)

print(type(stock))

for i in stock,stock2:
    if stock==stock2:
        print('Great you crashed market')

    elif stock < stock2:
        print('Ohh Shit the stock is down :(')

    elif stock > stock2:
        print('Great the the Stocks are smarter :)')

    elif stock != stock2:
        print('You Have Losted all your investment')

    else:
        print('Ahh,Great Atlast you make it happen !')


        



