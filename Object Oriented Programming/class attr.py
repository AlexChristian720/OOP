class Myclass(object):
    classy='class Value'

dd=Myclass()
print(dd.classy)#This Should Return The String "class-value"

dd.classy="Instance-Value"
print(dd.classy)#Return The String "Instance Value"

'''This Will Delete the value set for 'dd.classy' in the instance'''''

del dd.classy

#Since the overridding attr was deleted, this will print "class-value"

print(dd.classy)
