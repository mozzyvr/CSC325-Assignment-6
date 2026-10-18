import math
from triangle import is_valid_triangle, classify_triangle

# Negative/Zero Length Tests
def test_invalid_zero_length():
    assert classify_triangle(0, 1, 1) == "Invalid", "a = zero"
    assert classify_triangle(1, 0, 1) == "Invalid", "b = zero"
    assert classify_triangle(1, 1, 0) == "Invalid", "c = zero"

def test_invalid_negative_length():
    assert classify_triangle(-1, 1, 1) == "Invalid", "a = negative"
    assert classify_triangle(1, -1, 1) == "Invalid", "b = negative"
    assert classify_triangle(1, 1, -1) == "Invalid", "c = negative"

# Triangle Inequality Tests
def test_invalid_triangle_inequality():
    assert classify_triangle(1, 2, 10) == "Invalid", "fails a + b > c"
    assert classify_triangle(1, 10, 2) == "Invalid", "fails a + c > b"
    assert classify_triangle(10, 1, 2) == "Invalid", "fails b + c > a"

def test_valid_triangle():
    assert is_valid_triangle(3, 4, 5) is True, "3-4-5 is valid"

def test_degenerate_triangle():
    assert is_valid_triangle(1, 2, 3) is False, "degenerate (a + b == c) must not be valid"
    assert classify_triangle(1, 2, 3) == "Invalid", "degenerate, c longest (a + b == c) must be Invalid"
    assert classify_triangle(1, 3, 2) == "Invalid", "degenerate, b longest (a + c == b) must be Invalid"
    assert classify_triangle(3, 1, 2) == "Invalid", "degenerate, a longest (b + c == a) must be Invalid"

# Classification Tests
def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral", "integer sides"
    assert classify_triangle(2.5, 2.5, 2.5) == "Equilateral", "float sides"
 
def test_isosceles():
    assert classify_triangle(5, 5, 3) == "Isosceles", "equal pair first"
    assert classify_triangle(5, 3, 5) == "Isosceles", "equal pair split"
    assert classify_triangle(3, 5, 5) == "Isosceles", "equal pair last"
 
def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene", "sorted input"
    assert classify_triangle(6, 4, 5) == "Scalene", "unsorted input"
 
# Right Triangle Tests
def test_right_scalene():
    assert classify_triangle(3, 4, 5) == "Right Scalene", "3-4-5"
    assert classify_triangle(5, 3, 4) == "Right Scalene", "hypotenuse not last"
    assert classify_triangle(5, 12, 13) == "Right Scalene", "5-12-13"

def test_right_triangle():
    # (5*sqrt(2))**2 == 50.00000000000001
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles", "legs 5, 5, hypotenuse 5*sqrt(2)"
