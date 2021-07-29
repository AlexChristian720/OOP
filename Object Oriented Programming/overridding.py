class Thought(object):
    def __init__(self):
        pass
    def message(self):
        print('Thought, always Come and go')

class Advice(Thought):
    def __init__(self):
        super(Advice, self).__init__()

    def message(self):
        print('Warning: Risk Is Always involved when you are dealing with market')

