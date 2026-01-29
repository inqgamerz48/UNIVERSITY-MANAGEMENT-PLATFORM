import pytest
from services.grading import get_grade_point

def test_get_grade_point():
    assert get_grade_point(95, 100) == 10.0
    assert get_grade_point(85, 100) == 9.0
    assert get_grade_point(45, 100) == 5.0
    assert get_grade_point(30, 100) == 0.0

# Mock classes to simulate DB objects
class MockSubject:
    def __init__(self, credits):
        self.credits = credits

class MockMark:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score

# Note: Testing calculate_sgpa requires mocking AsyncSession which is complex.
# For this prototype, we focus on pure logic functions or integration tests.
