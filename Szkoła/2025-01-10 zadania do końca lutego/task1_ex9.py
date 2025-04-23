print("Cześć! Ten program wyświetli dla Ciebie liczby od 1 do 200, zamieniając liczby podzielne przez 7 na słowo 'boom'")
# Pytanie, czy użytkownik chce rozpocząć
start = input("Czy chcesz rozpocząć? (t/n): ")
if start.lower() != 't':
    print("No to pa!")
else:
    # Zakres liczb do 200
    for number in range(1, 201):
        if number % 7 == 0:
            print("boom")
        else:
            print(number)