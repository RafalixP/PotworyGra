import json

points = 0

def show_question(question):
    global points
    print()
    print(question["pytanie"])
    print('A: ', question["a"])
    print('B: ', question["b"])
    print('C: ', question["c"])
    print('D: ', question["d"])
    print()

    answer = input('Podaj prawidłową odpowiedź: ')

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("To prawidłowa odpowiedź, brawo! Masz już", points, "punktów.")
    else:
        print("Niestety to zła odpowiedź, prawidłowa odpowiedź to " + question["prawidlowa_odpowiedz"] + ".")

with open('JaknNauczycSieProgramowania\quiz.json', 'r') as json_file:
    questions = json.load(json_file)

    #print(questions)
    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print('To koniec gry. Zdobyłeś', points, 'punktów.')
