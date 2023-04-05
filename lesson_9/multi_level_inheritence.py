"""
C
B
A
"""

class A:

    def __init__(self):
        print("From Class A")

class B(A):

    def __init__(self):
        print("From Class B")
        A.__init__(self)

class C(B):
    def __init__(self):
        print("From Class C")
        B.__init__(self)


object_c = C()