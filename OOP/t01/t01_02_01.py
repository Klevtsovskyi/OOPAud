from math import inf


class QuadraticEquation:

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def show(self):
        print(f"{self._a} x^2 + {self._b} x + {self._c} = 0")

    def discriminant(self):
        return self._b ** 2 - 4 * self._a * self._c

    def solve(self):
        if self._a == self._b == self._c == 0:
            return inf

        if self._a == self._b == 0 and self._c != 0:
            return []

        if self._a == 0:
            return [-self._c / self._b]

        d = self.discriminant()
        if d < 0:
            return []
        elif d == 0:
            return [-self._b / (2 * self._a)]
        else:
            return [
                (-self._b - d ** 0.5) / (2 * self._a),
                (-self._b + d ** 0.5) / (2 * self._a),
            ]


if __name__ == '__main__':
    for i in range(1, 4):
        f = open(f"input0{i}.txt")
        print(f"input0{i}.txt")
        max_equation = None
        max_solution = -inf
        min_equation = None
        min_solution = inf

        for line in f:
            try:
                a, b, c = [int(x) for x in line.split()]
            except ValueError:
                continue
            q = QuadraticEquation(a, b, c)
            q.show()
            solutions = q.solve()
            print(solutions)
            if solutions is not inf and len(solutions) == 1:
                if solutions[0] < min_solution:
                    min_solution = solutions[0]
                    min_equation = q
                if solutions[0] > max_solution:
                    max_solution = solutions[0]
                    max_equation = q

        print("MIN:")
        min_equation.show()
        print(min_solution)
        print("MAX:")
        max_equation.show()
        print(max_solution)
        print()
        f.close()
