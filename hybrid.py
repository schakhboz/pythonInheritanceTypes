"""Inheritance consisting of multiple types of inheritance is called hybrid inheritance."""

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
        return self.b

class C(A):
    def __init__(self, a, c):
        self.c = c

        A.__init__(self, a)

    def getC(self):
        return self.c

class D(C):
    def __init__(self, a, c, d):
        self.d = d

        C.__init__(self, a, c)

    def getD(self):
        return self.a + self.c + self.d




