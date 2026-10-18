from triangle import classify_triangle

# Acceptance Criteria Tests

# Happy path
def test_buildable_triangle():
    assert classify_triangle(4, 5, 6) != "Invalid", "Triangle is buildable"

# Unhappy path that returns a string instead of raising an exception
def test_unbuildable_triangle():
    assert classify_triangle(1, 2, 10) == "Invalid", "Triangle is unbuildable"

# Flag right triangles since they do not need reinforced corners
def test_flag_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene", "Flagged: Right angle pieces need reinforced corners"