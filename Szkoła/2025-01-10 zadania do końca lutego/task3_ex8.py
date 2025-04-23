print('Program dzielący teksty na oddzielne słowa')
print()

def word_splitter(text):
    """
    Funkcja, która dzieli wejściowego stringa na oddzielne słowa
    
    :param text: parametr wejściowy - tekst
    :return: Lista słów z ciągu wejściowego
    """
    words = text.split()
    return words

# Przykładowe dane wejściowe
input_text = "To jest mój przykładowy tekst, przyjemnego czytania życzę"

# Użycie funkcji generatora do podzielenia tekstu na słowa i konwersja wyniku na listę
output_list = list(word_splitter(input_text))

print(output_list)