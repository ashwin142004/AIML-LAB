from itertools import permutations

def solve_cryptarithm(equation):
    letters = sorted(set(filter(str.isalpha, equation)))
    if len(letters) > 10:
        return None
    for perm in permutations(range(10), len(letters)):
        assign = dict(zip(letters, perm))
        expr = equation
        for l, d in assign.items():
            expr = expr.replace(l, str(d))
        try:
            left, right = expr.split('=')
            if eval(left) == eval(right):
                return assign
        except:
            continue
    return None

eq = input("Enter equation: ")
sol = solve_cryptarithm(eq)
if sol:
    print("Solution:", *[f"{k}={v}" for k, v in sol.items()])
else:
    print("No valid solution found")
