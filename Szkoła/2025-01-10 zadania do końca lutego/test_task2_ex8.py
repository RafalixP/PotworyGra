import pytest
import string
from task2_ex8 import generate_password

# Test sprawdzający, czy wygenerowane hasło spełnia wszystkie wymagania
def test_generate_password():
    for _ in range(100):  # Wygenerowanie 100 haseł w celu oceny poprawności działania pod kątem wymagań jakie spełniać powinno hasło
        password = generate_password()
        assert 6 <= len(password) <= 24, "Długość hasła nie mieści się w wymaganym zakresie."
        assert any(c in string.ascii_lowercase for c in password), "Hasło nie zawiera małej litery."
        assert any(c in string.ascii_uppercase for c in password), "Hasło nie zawiera wielkiej litery."
        assert any(c in "!%$#@?" for c in password), "Hasło nie zawiera znaku specjalnego."

# Sprawdzenie unikalności generowanych haseł
def test_multiple_password_generations():
    passwords = set(generate_password() for _ in range(100))  #set może zawierać wyłącznie elementy unikalne
    assert len(passwords) == 100, "Wygenerowane hasła nie są unikalne."

# Test przypadków brzegowych dla minimalnej i maksymalnej długości hasła
def test_edge_cases():
    min_length_password = generate_password()
    max_length_password = generate_password()
    
    while len(min_length_password) != 6:
        min_length_password = generate_password()
    while len(max_length_password) != 24:
        max_length_password = generate_password()
    
    assert 6 <= len(min_length_password) <= 24, "Minimalna długość hasła nie mieści się w wymaganym zakresie."
    assert 6 <= len(max_length_password) <= 24, "Maksymalna długość hasła nie mieści się w wymaganym zakresie."

# Uruchomienie testów
if __name__ == "__main__":
    pytest.main()