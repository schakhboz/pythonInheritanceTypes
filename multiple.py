
"""When a class can be derived from more than one base class this type of inheritance is called multiple inheritance.
In multiple inheritance, all the features of the base classes are inherited into the derived class. """

class A:
    def __init__(self, a):
        self.a = a

    def getA(self):
        return self.a


class B:
    def __init__(self, b):
        self.b = b

    def getB(self):
        return self.b


class C(A, B):
    def __init__(self, c, a, b):
        self.c = c

        A.__init__(self, a)
        B.__init__(self, b)

    def getC(self):
        return self.c + self.a + self.b
