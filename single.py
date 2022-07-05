"""Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code
reusability and the addition of new features to existing code. """

class A:
    def __init__(self, a):
        self.a = a

    def getA(self):
        return self.a


class B(A):
    def __init__(self, b, a):
        self.b = b
        A.__init__(self, a)

    def getB(self):
        return self.a + self.b
