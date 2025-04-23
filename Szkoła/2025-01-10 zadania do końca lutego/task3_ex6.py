# moduł statystyczny

#importujemuy niezbędne moduły
import math
from typing import List

#funkcja licząca średnią arytmetyczną
def arithmetic_average(numbers: List[float]) -> float:  #funkcja przyjmuje jako argument listę liczb
    """
    Oblicza średnią arytmetyczną listy liczb.
    
    :param numbers: Lista liczb
    :return: Średnia arytmetyczna

    Poniżej przypadki testowe:
    >>> arithmetic_average([1, 2, 3, 4, 5])
    3.0
    >>> arithmetic_average([10, 20, 30])
    20.0
    """
    return sum(numbers) / len(numbers)  #funkcja zwraca średnią arytmetyczną

#funkcja licząca średnią harmoniczną
def harmonic_average(numbers: List[float]) -> float:
    """
    Oblicza średnią harmoniczną listy liczb.
    
    :param numbers: Lista liczb
    :return: Średnia harmoniczna
    
    Poniżej przypadki testowe:
    >>> harmonic_average([1, 2, 3, 4, 5])
    2.18978102189781
    >>> harmonic_average([10, 20, 30])
    16.363636363636363
    """
    return len(numbers) / sum(1 / x for x in numbers)

#funkcja licząca średnią  geometryczną
def geometric_mean(numbers: List[float]) -> float:
    """
    Oblicz średnią geometryczną listy liczb.
    
    :param numbers: Lista liczb
    :return: Średnia geometryczna

    Poniżej przypadki testowe:    
    >>> geometric_mean([1, 2, 3, 4, 5])
    2.605171084697352
    >>> geometric_mean([10, 20, 30])
    18.171205928321395
    """
    product = math.prod(numbers)
    return product ** (1 / len(numbers))

#funkcja licząca średnią kwadratową
def mean_square(numbers: List[float]) -> float:
    """
    Oblicz średnią kwadratową listy liczb.
    
    :param numbers: Lista liczb
    :return: Średnia kwadratowa

    Poniżej przypadki testowe:    
    >>> mean_square([1, 2, 3, 4, 5])
    11.0
    >>> mean_square([10, 20, 30])
    466.6666666666667
    """
    return sum(x ** 2 for x in numbers) / len(numbers)

if __name__ == "__main__":
    #importujemy i uruchamiamy doctest
    import doctest
    doctest.testmod()