#import test framework
import pytest

# Import from the application file
from task1_ex11 import calculate_bmr, calculate_caloric_needs, calculate_caloric_difference, dishes

def test_calculate_bmr():
    assert calculate_bmr(70, 175, 25, 'm') == 1673.75
    assert calculate_bmr(60, 165, 30, 'k') == 1320.25
    assert calculate_bmr(80, 180, 40, 'm') == 1730.0
    assert calculate_bmr(55, 160, 20, 'k') == 1289.0

def test_calculate_caloric_needs():
    assert calculate_caloric_needs(1668.75, 'niski') == 2002.5
    assert calculate_caloric_needs(1371.25, 'średni') == 2125.4375
    assert calculate_caloric_needs(1820.0, 'wysoki') == 3139.5

def test_calculate_caloric_difference():
    assert calculate_caloric_difference(2000, 2500) == 500
    assert calculate_caloric_difference(1800, 1500) == -300
    assert calculate_caloric_difference(2200, 2200) == 0

def test_user_input_handling():
    age = 25
    weight = 70
    height = 175
    gender = 'm'
    activity_level = 'średni'
    selected_dishes = [1, 3, 5]

    bmr = calculate_bmr(weight, height, age, gender)
    caloric_needs = calculate_caloric_needs(bmr, activity_level)
    caloric_intake = sum(dishes[dish][1] for dish in selected_dishes)
    caloric_difference = calculate_caloric_difference(caloric_needs, caloric_intake)

    assert bmr == 1673.75
    assert caloric_needs == 2594.3125
    assert caloric_intake == 850
    assert caloric_difference == -1744.3125

if __name__ == "__main__":
    pytest.main()