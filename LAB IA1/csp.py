import itertools

def is_valid_solution(permutation, letters, equation):
    """Check if a given digit-letter mapping satisfies the equation."""
    letter_to_digit = dict(zip(letters, permutation))
    transformed_equation = equation

    for letter, digit in letter_to_digit.items():
        transformed_equation = transformed_equation.replace(letter, str(digit))

    left_side, right_side = transformed_equation.split('=')

    # Ensure no number has leading zeros (except for single-digit numbers)
    if any(part[0] == '0' and len(part) > 1 for part in left_side.split('+') + [right_side]):
        return False

    # Evaluate the equation
    try:
        return eval(left_side) == eval(right_side)
    except Exception:
        return False

def solve_cryptarithm(equation):
    """Solve the cryptarithm and return the first valid solution."""
    letters = sorted(set(filter(str.isalpha, equation)))
    if len(letters) > 10:
        raise ValueError("Too many unique letters (>10), cannot map to digits 0-9.")

    for perm in itertools.permutations(range(10), len(letters)):
        if is_valid_solution(perm, letters, equation):
            return dict(zip(letters, perm))  # Return first valid solution

    return None  # No solution found

def main():
    # Use a valid cryptarithm equation
    #equation = "BASE + BALL = GAMES"
    equation = input('Enter the equation:(eg. BASE + BALL = GAMES) : ')

    solution = solve_cryptarithm(equation)

    if solution:
        print(f"Solution for '{equation}':")
        for letter, digit in sorted(solution.items()):
            print(f"{letter} = {digit}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

