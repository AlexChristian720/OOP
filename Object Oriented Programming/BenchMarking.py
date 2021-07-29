import timeit

def testme(this_dict,key):
    return this_dict[key]

print(timeit.timeit("testme(mydict,key)",setup="from __main__ import testme; mydict={'a':9,'b':18,'c':27}; key='c'",number=1000000))
