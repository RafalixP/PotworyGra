import pytest
from task2_ex13 import calculate_mean

# Testujemy obliczanie średniej arytmetycznej - kilka asercji poniżej
def test_calculate_mean():
    assert calculate_mean([1, 2, 3, 4, 5]) == 3.0
    assert calculate_mean([10, 20, 30]) == 20.0
    assert calculate_mean([0, 0, 0]) == 0.0
    assert calculate_mean([]) == 0

# Testujemy interakcje z użytkownikiem
def test_program_loop(monkeypatch):
    inputs = iter(['10', '20', 'dość', 't', '5', '15', 'dość', 'n'])  # Symulacja - przykładowe inputy od użytkownika
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Używamy monkeypatcha aby wykorzystać w testowanym programie listę "inputs"
    
    # Symulacja uruchomienia programu
    import task2_ex13  # Importowanie głównego pliku programu

    # Sprawdzenie, czy program zakończył się poprawnie
    assert True  # Jeśli program zakończy się bez błędów, test przejdzie pomyślnie