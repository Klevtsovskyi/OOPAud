from QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):

    def __init__(self, a: float, b: float, c: float):
        super().__init__(a, b, c)

    def __str__(self):
        return f"{self._a} x^4 + {self._b} x^2 + {self._c} = 0"

    def solve(self) -> set[float] | float:
        sols = super().solve()
        if sols is self.INF:
            return self.INF
        elif len(sols) == 0:
            return sols
        else:
            result = set()
            for t in sols:
                eq = QuadraticEquation(1, 0, -t)
                result.update(eq.solve())
            return result


if __name__ == '__main__':
    eq = BiQuadraticEquation(1, -4, 2)
    eq.show()
    print(eq.solve())
