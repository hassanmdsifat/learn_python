

class A:

    def __init__(self):
        print("From Class A")

class B:

    def __init__(self):
        print("From Class B")

class C(A, B):
    def __init__(self):
        print("From class C")
        A.__init__(self)
        B.__init__(self)


object_c = C()