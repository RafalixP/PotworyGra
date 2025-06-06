# Program do obliczania średniej z liczb zapisanych w pliku 'dane_do_programu_1.txt' (założenie: otwieramy plik .txt z tej samej lokalizacji w której znajduje się plik .py)

def calculate_average_from_file(filename):
    # Otwieramy plik do odczytu
    with open(filename, 'r') as f:
        # Czytamy liczby z pliku i konwertujemy je na int
        numbers = [int(line.strip()) for line in f]
    # Obliczamy średnią
    return sum(numbers) / len(numbers)

# przypisujemy zmiennej nazwę pliki
filename = 'dane_do_programu_1.txt'
# przypisujemy zmiennej wynik działania funkcji calculate_average_from_file
average = calculate_average_from_file(filename)
# Wyświetlamy wynik
print(f"Wartość średnia liczb w pliku {filename} wynosi {average}.")