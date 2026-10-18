import math

def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """Return whether three side lengths form a non-degenerate triangle."""
    if a <= 0 or b <= 0 or c <= 0:
        return False

    return a + b > c and a + c > b and b + c > a

def classify_triangle(a: float, b: float, c: float) -> str:
    """Classify a triangle by side lengths and, when applicable, its right angle."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    sides = sorted((a, b, c))
    if sides[0] == sides[2]:
        classification = "Equilateral"
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        classification = "Isosceles"
    else:
        classification = "Scalene"

    if classification != "Equilateral" and math.isclose(
        sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2):
        return f"Right {classification}"

    return classification