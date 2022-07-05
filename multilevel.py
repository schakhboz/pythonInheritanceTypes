"""In multilevel inheritance, features of the base class and the derived class are further inherited into the new
derived class. This is similar to a relationship representing a child and grandfather. """

class A:
    def __init__(self, a):
        self.a = a

    def getA(self):
        return self.a


class B(A):
    def __init__(self, a, b):
        self.b = b
        A.__init__(self, a)

    def getB(self):
        return self.b + self.a


class C(B):
    def __init__(self, a, b, c):
        self.c = c
        B.__init__(self, a, b)

    def getC(self):
        return self.c + self.b + self.a