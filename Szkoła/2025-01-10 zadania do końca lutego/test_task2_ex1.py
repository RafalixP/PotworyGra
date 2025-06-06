import pytest

# Function to simulate user input and capture output
def run_password_program(inputs):
    from task2_ex1 import main  # the main script is named task2_ex1.py and has a main() function
    input_values = iter(inputs)
    
    def mock_input(prompt):
        return next(input_values)
    
    return main(mock_input)

def test_passwords_match():
    inputs = ["password123", "password123"]
    output = run_password_program(inputs)
    assert "Brawo, hasła są takie same." in output

def test_passwords_do_not_match():
    inputs = ["password123", "password456"]
    output = run_password_program(inputs)
    assert "Błąd: Hasła nie są takie same." in output