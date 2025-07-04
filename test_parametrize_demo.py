import pytest

# Simple parametrized test
@pytest.mark.parametrize("number,expected", [
    (2, 4),    # 2 * 2 = 4
    (3, 9),    # 3 * 3 = 9
    (4, 16),   # 4 * 4 = 16
    (5, 25),   # 5 * 5 = 25
])
def test_square_numbers(number, expected):
    """Test that number squared equals expected"""
    result = number * number
    print(f"Testing: {number}² = {result} (expected {expected})")
    assert result == expected

# Multiple parameters
@pytest.mark.parametrize("name,age,valid", [
    ("Alice", 25, True),
    ("Bob", 17, False),   # Under 18
    ("Charlie", 30, True),
])
def test_adult_check(name, age, valid):
    """Test adult age validation"""
    is_adult = age >= 18
    print(f"{name} (age {age}) is adult: {is_adult}")
    assert is_adult == valid