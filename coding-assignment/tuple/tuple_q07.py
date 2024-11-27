# How can you use tuples to implement a simple version of a set data structure?


class SimpleSet:
    def __init__(self):
        self.data = ()

    def add(self, element):
        if element not in self.data:
            self.data += (element,)

    def remove(self, element):
        self.data = tuple(item for item in self.data if item != element)

    def __contains__(self, element):
        return element in self.data

    def __str__(self):
        return str(self.data)

s = SimpleSet()
s.add(1)
s.add(2)
s.add(2)
print(s)  
