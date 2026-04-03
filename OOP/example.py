class A:

    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def get(self):
        return f"{self.a} {self._b} {self.__c}"

    def show(self):
        print(f"A: {self.get()}")


class B(A):

    def show(self):
        print(f"B: {self.get()}")
        super().show()


if __name__ == '__main__':
    obj_a = A(432, 542, 103)
    obj_a.show()

    obj_b = B(123, 234, 654)
    obj_b.show()
