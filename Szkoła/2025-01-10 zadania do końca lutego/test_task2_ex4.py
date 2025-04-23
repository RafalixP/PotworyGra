import pytest
import io
import contextlib

# Function to simulate user input and capture output
def run_time_program(inputs):
    from task2_ex4.py import main  # the main script is named task2_ex4.py and has a main() function
    input_values = iter(inputs)
    
    def mock_input(prompt):
        return next(input_values)
    
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        main(mock_input)
    return output.getvalue()

def test_valid_input():
    inputs = ["12:00", "00:15", "koniec"]
    output = run_time_program(inputs)
    assert "Liczba kwadransów zawierająca się w podanym czasie: 48" in output
    assert "Liczba kwadransów zawierająca się w podanym czasie: 1" in output
    assert "Do widzenia!" in output

def test_invalid_input_format():
    inputs = ["abc", "koniec"]
    output = run_time_program(inputs)
    assert "Błąd: Upewnij się, że czas jest poprawnie podany w formacie HH:MM." in output
    assert "Do widzenia!" in output

def test_mixed_valid_and_invalid_input():
    inputs = ["12:00", "abc", "00:30", "koniec"]
    output = run_time_program(inputs)
    assert "Liczba kwadransów zawierająca się w podanym czasie: 48" in output
    assert "Błąd: Upewnij się, że czas jest poprawnie podany w formacie HH:MM." in output
    assert "Liczba kwadransów zawierająca się w podanym czasie: 2" in output
    assert "Do widzenia!" in output