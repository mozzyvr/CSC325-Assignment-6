# CSC325 Module 6 Assignment

## Equivalence Classes and Boundaries

### Overview

If a triangle is equilateral, all angles are 60 degrees. The three angles of a triangle must sum to 180 degrees so equilateral triangles can never have a 90 degree angle (right triangle)

### Table

| Class | Representative Tests | Expected |
| --- | --- | --- |
| A side is zero | (0, 1, 1), (1, 0, 1), (1, 1, 0) | Invalid |
| A side is negative | (-1, 1, 1), (1, -1, 1), (1, 1, -1) | Invalid |
| Fails triangle inequality | (1, 2, 10), (1, 10, 2), (10, 1, 2) | Invalid |
| All sides equal | (5, 5, 5), (2.5, 2.5, 2.5) | Equilateral |
| Exactly two sides equal | (5, 5, 3), (5, 3, 5), (3, 5, 5) | Isosceles |
| All sides different | (4, 5, 6), (6, 4, 5) | Scalene |
| Satisfies Pythagorean theorem, all sides different | (3, 4, 5), (5, 3, 4), (5, 12, 13) | Right Scalene |
| Satisfies Pythagorean theorem, two sides equal | (5, 5, 5√2) | Right Isosceles |

### Boundaries

- **Side length at zero:** a side of exactly 0 is Invalid, tested in each position (a, b, c).
- **Triangle inequality at equality (degenerate):** when the two shorter sides sum exactly to the longest, the triangle is Invalid. Tested with the longest side in each position: (1, 2, 3), (1, 3, 2), (3, 1, 2).

## Copilot Review Log

| Test | Copilot Suggested? | Kept/Edited/Rejected | Why? |
| --- | --- | --- | --- |
| test_invalid_zero_length | Yes | Edited | Autocomplete only generated a test case for one side <= 0, performed test cases for each side of triangle | 
| test_right_triangle | Yes | Edited | Copilot used (5*sqrt(2))**2 == 50, which does not round properly because it is floating point. Changed the test to assert that (5*math.sqrt(2)) passes |
| test_equilateral_is_never_right | Yes | Rejected | Test is not able to fail, as stated in equilateral explanation within the README. | 
| All Test Functions | Yes | Edited | Added short strings to each test that explain what each assertion is testing for (Used Copilot Chat, see AI usage) |

## Prereqs / Running pytest

### Linux (Bash)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pytest -v
```
### Windows (Powershell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest -v
```
## Acceptance Criteria

- When 3 side lengths that form a triangle are entered, a classification other than "Invalid" is returned, showing the triangle is buildable
- When 3 numeric side lengths that cannot form a triangle are entered, "Invalid" is returned and no exception is raised
- Right angle pieces are flagged with `"Right <triangle-type>"`, since they need reinforced corners

## AI Usage

| Tool Used | Purpose | Changed/Verified |
| --- | --- | --- |
| GitHub Copilot Chat | Drafted is_valid_triangle and classify_triangle | Verified implementation against spec, removed explicit rel_tol variable (which is already used by default) |
| GitHub Copilot Chat | Used to draft descriptive failures for each written pytest | Verified that each one correctly matches each test case I wrote |
| GitHub Copilot | Used to draft README test instructions for Powershell users | Verified that the commands are accurate |
| GitHub Copilot | Drafted equivalence classes and boundaries based on written test cases | Edited and verified that all equivalance tests and boundaries are correct |