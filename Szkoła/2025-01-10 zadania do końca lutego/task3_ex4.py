# Analizuje plik i zwraca procentowy udział każdego znaku w tekście.

def count_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # otwieramy plik 'file_path'
            text = file.read()  # przypisujemy zawartość pliku zmiennej 'text'
    except FileNotFoundError:
        print(f"Błąd: Plik '{file_path}' nie został znaleziony.")
        return None
    except IOError:
        print(f"Błąd: Nie można otworzyć pliku '{file_path}'.")
        return None

    total_characters = len(text)  # całkowita ilość znaków w pliku
    character_counts = {}  # słownik w którym będziemy zapisywać znaki i ich poszczególne wystąpienia

    for char in text:  # iterujemy przez każdy kolejny znak tekstu
        if char == '\n':
            continue  # pomijanie znaków nowej linii
        if char in character_counts:  # jeśli dany znak znajduje się już w słowniku
            character_counts[char] += 1  # to dodajemy mu jedno wystąpienie
        else:  # jeśli nie znajduje się w słowniku
            character_counts[char] = 1  # to dopisujemy go do słownika i przypisujemy mu jedno wystąpienie

    # tworzymy nowy słownik 'character_percentages' w którym znajdą się pary znak - procentowy udział w tekście
    character_percentages = {char: (count / total_characters) * 100 for char, count in character_counts.items()}  # dla każdego znaku 'char' obliczamy i zapisujemy w tym słowniku jego procentowy udział

    return character_percentages

# Wyświetla procentowy udział każdego znaku w tekście.
def print_character_percentages(character_percentages):
    """
    :param character_percentages: Słownik z procentowym udziałem każdego znaku
    """
    for char, percentage in character_percentages.items():  # iterujemy przez słownik 'character_percentages'
        if char == '\n':
            char = '\\n'  # zamiana znaku nowej linii na czytelny format
        print(f"Znak '{char}' występuje w {percentage:.2f}% tekstu")

if __name__ == "__main__":
    print('Witaj w moim magicznym programie liczącym')
    print()
    while True:
        file_path = input("Podaj ścieżkę do pliku tekstowego: ")  # przypisujemy zmiennej 'file_path' ścieżkę do pliku podaną przez użytkownika
        char_percentages = count_characters(file_path)  # nowa zmienna której przypisujemy wartość zwracaną przez funkcję 'count_characters'
        if char_percentages:
            print_character_percentages(char_percentages)  # wyświetlamy wynik

        # Pytanie użytkownika, czy chce sprawdzić kolejny plik
        print()
        again = input("Czy chcesz sprawdzić kolejny plik? (t/n): ").strip().lower()
        print()
        if again != 't':
            print("Do widzenia, zapraszam ponownie.")
            break