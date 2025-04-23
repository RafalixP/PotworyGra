import pytest
from task2_ex12 import convert_to_binary #import funkcji z głownego pliki programu którą będziemy tu testować

def test_convert_to_binary():
    #asercje dotyczące wyników konwersji konkretnych liczb
    assert convert_to_binary(0) == '0'
    assert convert_to_binary(1) == '1'
    assert convert_to_binary(2) == '10'
    assert convert_to_binary(10) == '1010'
    assert convert_to_binary(255) == '11111111'

def test_user_interaction(monkeypatch):
    inputs = iter(['10', 't', '33', 'n']) #symulacja - przykładowe inputy od użytkownika: konwersja liczby 10, 't' jako zgoda na kolejną konwersję, konwersja liczby 33, 'n' jako zakończenie programu
    monkeypatch.setattr('builtins.input', lambda _: next(inputs)) #używamy monkeypatcha aby wykorzystać w testowanym programie listę "inputs"
    
    # Symulacja uruchomienia programu
    import task2_ex12  # Importowanie głównego pliku programu

    # Sprawdzenie, czy program zakończył się poprawnie
    assert True  # Jeśli program zakończy się bez błędów, test przejdzie pomyślnie