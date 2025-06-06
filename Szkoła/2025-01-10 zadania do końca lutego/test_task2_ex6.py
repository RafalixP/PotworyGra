import pytest
from task2_ex6 import greet_user, caesar_cipher

# Test funkcji caesar_cipher
def test_caesar_cipher():
    # Przypadek testowy: przesunięcie o 3
    assert caesar_cipher("abc", 3) == "def"
    assert caesar_cipher("xyz", 3) == "abc"
    assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"

    # Przypadek testowy: przesunięcie o -3
    assert caesar_cipher("def", -3) == "abc"
    assert caesar_cipher("abc", -3) == "xyz"
    assert caesar_cipher("Khoor, Zruog!", -3) == "Hello, World!"

    # Przypadek testowy: przesunięcie o 0 (bez zmian)
    assert caesar_cipher("unchanged", 0) == "unchanged"
    
    # Przypadek testowy: znaki niealfabetyczne pozostają niezmienione
    assert caesar_cipher("1234!@#$", 5) == "1234!@#$"

# Test funkcji greet_user
def test_greet_user(monkeypatch):
    # testowe dane wejściowe
    inputs = iter(["test text", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    text, shift = greet_user()
    assert text == "test text"
    assert shift == 3

if __name__ == "__main__":
    main()