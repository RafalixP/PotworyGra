#to jest to bardziej zaawansowane podejście

import pytest
from io import StringIO
from contextlib import redirect_stdout
from task2_ex12 import convert_to_binary  # Importowanie funkcji z pliku task2_ex12.py

def test_convert_to_binary():
    assert convert_to_binary(0) == '0'
    assert convert_to_binary(1) == '1'
    assert convert_to_binary(2) == '10'
    assert convert_to_binary(10) == '1010'
    assert convert_to_binary(255) == '11111111'

def test_program_output(monkeypatch):
    inputs = iter(['10', 'n'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    f = StringIO()
    with redirect_stdout(f):
        import task2_ex12  # Importowanie głównego pliku programu
    
    output = f.getvalue().split('\n')
    assert "Cześć! Ten program konwertuje liczby dziesiętne na system binarny." in output
    assert "Podaj liczbę, którą chcesz przekonwertować na system binarny: " in output
    assert "Liczba 10 w systemie binarnym to: 1010" in output
    assert "Czy chcesz przekonwertować kolejną liczbę? (t/n): " in output
    assert "Dziękuję za skorzystanie z programu! Do zobaczenia!" in output