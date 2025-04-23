import doctest
from task3_ex9 import Stork

def run_tests():
    """
    Uruchamia testy dla klasy Stork.
    """
    doctest.testmod()
    print("Wszystkie testy przeszły pomyślnie!")

if __name__ == "__main__":
    # Tworzymy obiekt bocian_1 korzystający z wartości domyślnych dla klasy Stork
    bocian_1 = Stork()

    # Dodaj testy do docstringów metod klasy Stork
    bocian_1.set_color("yellow")
    assert bocian_1.get_color() == "yellow"

    bocian_1.set_position([15, 10])
    assert bocian_1.get_position() == (15, 10)

    try:
        bocian_1.set_position([15, -10])
    except ValueError as e:
        assert str(e) == "Współrzędna y nie może być ujemna."

    try:
        bocian_1.set_position([15])
    except ValueError as e:
        assert str(e) == "Pozycja musi być listą składającą się z dwóch elementów."

    try:
        bocian_1.set_position("15, 10")
    except ValueError as e:
        assert str(e) == "Pozycja musi być listą składającą się z dwóch elementów."

    try:
        bocian_1.set_position([15, "10"])
    except ValueError as e:
        assert str(e) == "Oba elementy pozycji muszą być liczbami."

    # Uruchom testy doctest
    run_tests()