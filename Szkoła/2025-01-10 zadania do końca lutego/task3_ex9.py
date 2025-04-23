class Stork:
    def __init__(self, color="brown", position=(0, 0)):
        self.color = color
        self.position = position

    def get_color(self):
        """
        Zwraca kolor bociana.
        
        >>> bocian_1.get_color()
        'brown'
        """
        return self.color

    def set_color(self, new_color):
        """
        Zmienia kolor bociana na inny zadany
        
        >>> bocian_1.set_color("yellow")
        >>> bocian_1.get_color()
        'yellow'
        """
        self.color = new_color

    def get_position(self):
        """
        Zwraca pozycję bociana.
        
        >>> bocian_1.get_position()
        (0, 0)
        """
        return self.position

    def set_position(self, new_position):
        """
        Wprowadza nową pozycję bociana.
        
        >>> bocian_1.set_position([15, 10])
        >>> bocian_1.get_position()
        (15, 10)
        
        >>> bocian_1.set_position([15, -10])
        Traceback (most recent call last):
            ...
        ValueError: Współrzędna y nie może być ujemna.
        
        >>> bocian_1.set_position([15])
        Traceback (most recent call last):
            ...
        ValueError: Pozycja musi być listą składającą się z dwóch elementów.
        
        >>> bocian_1.set_position("15, 10")
        Traceback (most recent call last):
            ...
        ValueError: Pozycja musi być listą składającą się z dwóch elementów.
        
        >>> bocian_1.set_position([15, "10"])
        Traceback (most recent call last):
            ...
        ValueError: Oba elementy pozycji muszą być liczbami.
        """
        if not isinstance(new_position, list) or len(new_position) != 2:
            raise ValueError("Pozycja musi być listą składającą się z dwóch elementów.")
        
        if not all(isinstance(coord, (int, float)) for coord in new_position):
            raise ValueError("Oba elementy pozycji muszą być liczbami.")
        
        if new_position[1] < 0:
            raise ValueError("Współrzędna y nie może być ujemna.")
        
        self.position = tuple(new_position)

# Tworzymy obiekt bocian_1 korzystający z wartości domyślnych dla klasy Stork
bocian_1 = Stork()

# Uruchamiamy testy używając doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()