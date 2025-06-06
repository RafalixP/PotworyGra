import random

def quiz_app():
    '''Quiz z losowymi pytaniami'''

    # Słownik z 20 pytaniami i poprawnymi odpowiedziami
    questions = {
        1: ("Jaki kolor może przyjąć różowa pantera?", "Bladoróżowy"),
        2: ("Czy dziś jest słonecznie?", "nie"),
        3: ("Kto uchodzi za wynalazcę telefonu (podaj nazwisko)?", "Bell"),
        4: ("Jakim środkiem z domowej kuchni można zabezpieczyć stal przed oksydacją?", "olej"),
        5: ("Czy do zawieszenia obrazka na ścianie warto użyć kołka rozporowego z pasującym wkrętem lub hakiem?", "tak"),
        6: ("Czy regulowane biurka zawsze są stabilne?", "nie"),
        7: ("Czy warto pić dużo wody?", "tak"),
        8: ("Czy w tym roku będzie śnieg?", "Pomidor"),
        9: ("Jakie warzywo kojarzy się ze słoneczną Italią?", "Pomidor"),
        10: ("Czy krowy mogą latać?", "nie"),
        11: ("Jakie zwierzę jest znane z tego, że śpi na jednej nodze?", "Flaming"),
        12: ("Czy można zjeść zupę widelcem?", "nie"),
        13: ("Czy jednorożce istnieją?", "nie"),
        14: ("Jakie jest ulubione jedzenie pand?", "Bambus"),
        15: ("Czy można jeździć na rowerze pod wodą?", "nie"),
        16: ("Czy koty mają dziewięć żyć?", "nie"),
        17: ("Jakie zwierzę jest znane z tego, że zmienia kolor?", "Kameleon"),
        18: ("Czy można zjeść pizzę na śniadanie?", "tak"),
        19: ("Czy ryby mogą oddychać powietrzem?", "nie"),
        20: ("Czy można tańczyć na księżycu?", "tak")
    }

    while True:
        # Pytanie, czy użytkownik chce rozpocząć quiz
        start = input("Zaczynamy (t/n)? ").strip().lower()
        if start != 't':
            print("\nDziękuję za grę.")
            break

        # Informacja dla użytkownika
        print("\nProszę podawać proste odpowiedzi, przykładowo: tak, nie lub rzeczownik w mianowniku.")

        # Losowanie 6 pytań z 20
        selected_questions = random.sample(list(questions.items()), 6)
        score = 0
        results = []

        for i, (number, (question, correct_answer)) in enumerate(selected_questions, 1):
            print(f"\nPytanie {i} z 6")
            print(f"{question}")
            user_answer = input("Twoja odpowiedź: ").strip().lower()

            if user_answer == correct_answer.lower():
                score += 1
                results.append((question, "Poprawna"))
            else:
                results.append((question, "Niepoprawna"))

        # Wyświetlanie wyniku
        print(f"\nTwój wynik: {score}/6")
        print()
        print('Twoje odpowiedzi:')
        for question, result in results:
            print(f"{question} - {result}")

        # Pytanie, czy użytkownik chce zagrać ponownie
        repeat = input("\nCzy chcesz zagrać ponownie? (t/n): ").strip().lower()
        if repeat != 't':
            print("\nDziękuję, do zobaczenia.")
            break

print()
print('Quiz z losowymi pytaniami')
print('-------------------------------------')

quiz_app()