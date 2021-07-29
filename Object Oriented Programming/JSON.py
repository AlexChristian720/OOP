import json

x=json.dumps({'x1':[2,4,6],'y1':[3,6,9],'z1':[4,8,2]})

print(x)


mystruct=json.loads(x)
for key in mystruct:
    print(key)
    for x in mystruct[key]:
        print(" {0}".format(x))
