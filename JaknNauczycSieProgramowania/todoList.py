user_choice = -1

tasks = []

def show_tasks():
    task_index = 0
    print()
    print('Lista zadań:')
    print()

    if len(tasks) == 0:
        print('--Brak zadań--')
        print()
    for task in tasks:
        print("[" + str(task_index) + "]" + task)

        task_index += 1
    print()

def add_task():
    task = input('Dodaj zadanie: ')
    tasks.append(task)
    print()
    print('Dodano zadanie')
    print()

def delete_task():
    task_index = int(input('Które zadanie chcesz usunąć? '))
    if task_index < 0 or task_index >= len(tasks):
        print('Nieprawidłowy numer zadania, zadanie o tym numerze nie istnieje')
        print()
        return
    tasks.pop(task_index)
    print('Usunięto zadanie')
    print()

def save_task_to_file():
    with open('JaknNauczycSieProgramowania\plik_todo.txt', 'w') as todo_file:
        for task in tasks:
            todo_file.write(task + '\n')


    '''file = open('JaknNauczycSieProgramowania\plik_todo.txt', 'w')
    for task in tasks:
        file.write(task + '\n')
    file.close()'''

def load_files_from_file():
    try:
        with open('JaknNauczycSieProgramowania\plik_todo.txt', 'r') as todo_file:
            for line in todo_file.readlines():
                tasks.append(line.strip())
    except FileNotFoundError:
        return
    
load_files_from_file()

while user_choice!= 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_task_to_file()
    if len(str(user_choice)) == 0:  # to jest NOK, do przemyślenia i poprawy
        print('Podaj PRAWIDŁOWY numer funkcji: ')

    print('1. Pokaż zadanie')
    print('2. Dodaj zadanie')
    print('3. Usuń zadanie')
    print('4. Zapisz zmiany do pliku')
    print('5. Wyjdź')

    user_choice = int(input('Podaj numer funkcji: '))

