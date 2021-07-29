class NegativeNumberException(RuntimeError):
    def __init__(self,age):
        super().__init__()
        self.age=age



