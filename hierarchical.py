"""When more than one derived classes are created from a single base this type of inheritance is called hierarchical
inheritance. In this program, we have a parent (base) class and two child (derived) classes. """


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


class C(A):
    def __init__(self, c, a):
        self.c = c
        A.__init__(self, a)

    def getC(self):
        return self.a + self.c
