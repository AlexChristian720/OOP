#Reveresed(seq

normal_list=[2,4,6,8,0]
class CustomSeQuence():
    def __len__(self):
        return 5
    def __getitem__(self, index):
        return "x{0}".format(index)

class FunckyBack():
    def __reversed__(self):
        return 'backwards'

for seq in normal_list,CustomSeQuence(),FunckyBack():
    print('\n{}: '.format(seq.__class__.__name__),end="")
    for item in reversed(seq):
        print(item,end=", ")
