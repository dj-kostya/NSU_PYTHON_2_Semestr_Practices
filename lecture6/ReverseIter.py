class ReverseIter:
    def __init__(self, array):
        if not isinstance(array, str) and not isinstance(array, list):
            raise ValueError("Not a list or a string")
        self.list = array
        self.i = len(self.list) - 1

    def __iter__(self):
        self.i = len(self.list) - 1
        return self

    def __next__(self):
        if self.i < 0:
            raise StopIteration
        self.i -= 1
        return self.list[self.i + 1]

# rev = ReverseIter('dsada')
# for i in rev:
#     print(i, end=' ')
# => a d a s d
