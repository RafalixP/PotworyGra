class BankAccount:
    def __init__(self, balance=0):  #domyślne saldo konta wynosi 0
        """
        Tworzy nowe konto bankowe z zadanym saldem.
        
        Przypadek testowy - obiekt testowy z saldem 250
        >>> account = BankAccount(250)
        >>> account.balance
        250
        """
        self.balance = balance  #przypisujemy wartość parametru balance do zmiennej instancji self.balance, inicjalizując saldo konta podaną wartością

    def add_funds(self, amount):
        """
        Dodaje środki do konta bankowego.
        
        Przypadek testowy - obiekt testowy z saldem 250, następnie dodanie 150 do salda
        >>> account = BankAccount(250)
        >>> account.add_funds(150)
        >>> account.balance
        400
        """
        self.balance += amount  #dodajemy wartość amount do bieżącego salda

    def combine_accounts(self, other_account):  #other_account to inna instancja klasy BankAccount
        """
        Łączy dwa konta bankowe z prowizją 5% za operację łączenia.
        
        Przypadki testowe:
        >>> account1 = BankAccount(400)
        >>> account2 = BankAccount(500)
        >>> account1.combine_accounts(account2)
        >>> account1.balance
        855.0
        >>> account2.balance
        0
        """
        total_balance = self.balance + other_account.balance    #całkowite saldo
        commission = total_balance * 0.05   # oblicza prowizję w wysokości 5% od całkowitego salda
        self.balance = total_balance - commission   #odlicza prowizję od salda konta 1
        other_account.balance = 0   #saldo konta 2 po połączeniu

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print("Wszystkie testy zakończone sukcesem!")
    else:
        print(f"{result.failed} testów nie powiodło się z {result.attempted}.")