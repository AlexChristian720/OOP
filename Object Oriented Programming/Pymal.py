import yaml,json

with open('eRecord.yaml') as fh:
    struct= yaml.load(fh)

print(struct)

print('--------------------------')
print('To Make the output more readable format, add the json module')
print(json.dumps(struct,indent=4,separators=(',',':')))