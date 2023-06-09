for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
    

s = 'abc'
it = iter(s)
it
# <str_iterator object at 0x10c90e650>
next(it)
# 'a'
next(it)
# 'b'
next(it)
# 'c'
next(it)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     next(it)
StopIteration


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
    
rev = Reverse('spam')
iter(rev)
# <__main__.Reverse object at 0x00A1DB50>
for char in rev:
    print(char)