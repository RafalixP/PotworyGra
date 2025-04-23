'''
Pomysły na rozwój apki:
1. Dodać opcję umożliwającą usunięcie od razu wszystkich zadań (w ramach istniejącej funkcji delete?) DONE
2. Dodać opcję umożliwającą usunięcie zakresu zadań (w ramach istniejącej funkcji delete?)
3. Dodać opcję przesortowania zadań tak aby przywrócić ciąglą numerację zadań
4. W funkcji delete dodać opcję wyjścia po wpisaniu X częściowo DONE
5. W funkcji delete zrobić tak aby po skasowaniu zadsania nie było powrotu do menu, lecz aby zostać w 
obrębie funkcji delete (ale z pytaniem o wyjście jak w punkcie wyżej) częściowo DONE

'''

import sqlite3

connection = sqlite3.connect('JaknNauczycSieProgramowania\db_todo.db')

def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass

def show_tasks(connection):
    
    while True:
        show_tasks_for_real(connection)

        print()
        # print('To jest kawałek kodu poza pętlą')
        user_choice = input('Wpisz S aby sortować zadania, lub wpisz X aby wrócić do menu: ')
        if user_choice == 'x':
            print('Powrót do menu')
            break

        elif len(user_choice) =='s':
            sort_tasks(connection)
            print('')
            print('OK, sortujemy...')

            # attempts_inside = 0
            # while attempts_inside < 1:
            #     attempts_inside += 1
            #     cur = connection.cursor()
            #     cur.execute("""SELECT rowid, task FROM task""")
            #     print('Oto lista Twoich zadań po sortowaniu: ')
            #     result = cur.fetchall()
            #     print()

                # if len(result) == 0:
                #     print('---brak zadań---')
                # else:
                #     for row in result:
                #         print(str(row[0]) + ' - ' + row[1])

        else:
            print('Nie ma takiej opcji. Wpisz S aby sortować zadania, lub wpisz X aby wrócić do menu ')
            pass

def show_tasks_for_real(connection):
    attempts = 0
    while attempts < 1:
        attempts += 1
        cur = connection.cursor()
        cur.execute("""SELECT rowid, task FROM task""")
        print('Oto lista Twoich zadań: ')
        result = cur.fetchall()
        print()

        if len(result) == 0:
            print('---brak zadań---')
        else:
            for row in result:
                print(str(row[0]) + ' - ' + row[1])

def sort_tasks(connection):
    print('')
    print('Tu będzie funkcje sortowania zadań') #placeholder na funkcję sortowania
def add_task(connection):

    print()
    task = input('Dodaj zadanie lub wpisz x aby wrócić: ') 
    #int_task = int(task)

    if task == 'x':
        print('Powrót do menu')
    else:   
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES (?)""", (task,))
        connection.commit()
        print('Dodano zadanie')

def delete_task(connection): #general_delete_funkction
    while True:
        print()
        print('Wpisz 1 aby usunąć jedno wybrane zadanie')
        print('Wpisz 2 aby usunąć wszystkie zadania')
        print('Wpisz X aby powrócić do głównego menu')
        user_choice = input()
        print()
        if len(user_choice) == 0:
            print()
            print('Wpisz COKOLWIEK.')
            continue

        attempts = 0

        if user_choice == 'x':
            break
        while user_choice != '' and attempts < 1:
            attempts += 1
            
            try:
                user_choice = int(user_choice)
            except:
                print('Please use numeric digits.')
                continue
            if user_choice < 1 or user_choice > 2:
                print('Please enter a valid number (from 1 to 2).')
                continue
            break

        if user_choice == 1:
            delete_one_task(connection)
            break
        if user_choice == 2:
            delete_all_tasks(connection)
            break
        


def delete_one_task(connection):
    task_index = input('Które zadanie chcesz usunąć? Wpisz numer zadania lub X aby powrócić: ')

    if str(lower(task_index)) == 'x':
        print('Wracam do menu...')
        print()
        # break
    
    cur = connection.cursor()
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowid=?""", (task_index,)).rowcount
    count_of_deleted = cur.rowcount
    connection.commit()
    print()
    if rows_deleted == 0:
        print('Nieprawidłowy numer zadania, zadanie o takim numerze nie istnieje')
        pass
    else:
        print('Usunięto ', count_of_deleted, ' zadanie')

    print()

def delete_all_tasks(connection):
    user_choice = input('Are you sure you want to delete? Y / N ').lower()
    if user_choice == 'y':
        cur = connection.cursor()
        rows_deleted = cur.execute("""DELETE FROM task WHERE 1 = 1 """)
        count_of_deleted = cur.rowcount
        connection.commit()
        print('Usunięto wszystkie zadania')
        print('Liczba usuniętych wierszy to: ', count_of_deleted)
        print()
    else:
        print()
        print('heh, rozmyśliłeś się...')

create_table(connection)

user_choice = 0

while True:
    
    print()
    print('--- MENU ---')
    print('1. Pokaż zadanie')
    print('2. Dodaj zadanie')
    print('3. Usuń zadanie')
    print('4. Wyjdź')
    print()
    our_input = input('Podaj numer funkcji: ')
    if len(our_input) == 0:
            print()
            print('Wpisz COKOLWIEK.')
            continue
    attempts = 0
    while our_input != '' and attempts < 1:
        attempts += 1
        
        try:
            user_choice = int(our_input)
        except:
            print('Please use numeric digits.')
            continue
        if user_choice < 1 or user_choice > 4:
            print('Please enter a valid number (from 1 to 4).')
            continue
        break

    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        break

connection.close()




