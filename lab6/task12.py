class A:
    def __str__(self):
        return "A: __str__ method"

    def hello(self):
        print("Hello")


class B:
    def __str__(self):
        return "B: __str__ method"

    def good_evening(self):
        print("Good evening")


class C(A, B):
    pass


class D(A, B):
    def __str__(self):
        return B.__str__(self)


if __name__ == "__main__":
    a = A()
    b = B()
    c = C()
    d = D()

    print(str(a))
    print(str(b))
    print(str(c))
    print(str(d))

    a.hello()
    b.good_evening()
    c.hello()
    c.good_evening()
    d.hello()
    d.good_evening()

