from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation


if __name__ == '__main__':
    f = open("input03.txt")
    equations = {
        0: [], 1: [], 2: [], 3: [], 4: [], Equation.INF: []
    }
    for line in f:
        args = [float(x) for x in line.split()]
        if len(args) == 2:
            eq = Equation(*args)
        elif len(args) == 3:
            eq = QuadraticEquation(*args)
        elif len(args) == 5:
            eq = BiQuadraticEquation(args[0], args[2], args[4])
        else:
            continue

        solutions = eq.solve()
        if solutions == Equation.INF:
            equations[Equation.INF].append(eq)
        else:
            equations[len(solutions)].append(eq)

    min_solution = Equation.INF
    max_solution = -Equation.INF
    min_equation = None
    max_equation = None
    for eq in equations[1]:
        solution = eq.solve().pop()
        if solution < min_solution:
            min_solution = solution
            min_equation = eq
        if solution > max_solution:
            max_solution = solution
            max_equation = eq

        print("MIN:")
        min_equation.show()
        print(min_solution)
        print("MAX:")
        max_equation.show()
        print(max_solution)
        print()


    f.close()