from enum import Enum


users = []


class BankAccount:
    __account: int = 0
    __currency: str = "KZT"

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_account(self):
        return self.__account

    def get_currency(self):
        return self.__currency

    def set_account(self, amount):
        self.__account = + amount

    def set_account_type(self, type):
        self.__currency = type

    def __del__(self):
        print('Destructor called, BankAccount deleted.')

    def __str__(self):
        return f"{self.name} {self.surname}"


# person = BankAccount(name="Fazil", surname="Sultan")
# print(person)
class Account(Enum):
    USD = "USD"
    KZT = "KZT"
    RUB = "RUB"


class USerOperations:

    def add(self, total, n):
        return total + n

    def sub(self, total, n):
        return total - n

    def todollar(self, total):
        dollar = total / 470

        return dollar

    def totenge(self, total):
        tenge = total * 470

        return tenge

    def toRubl(self, total):
        rubl = total * 70

        return rubl

    def fromRubl(self, total):
        rubl = total / 70

        return rubl


while True:
    print('''             1. Create user
             2. Find user
             0. Log out
    ''')


    n = int(input("Enter your choice "))
    match n:
        case 1:
            name = input("Enter your name:  ")
            surname = input("Enter your surname:  ")
            person = BankAccount(name, surname)
            users.append(person)
        case 2:
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            user = next(u for u in users if (u.name == name and u.surname == surname))
            if user is not None:
                while True:
                    print('''Choose your option
              1. Insert your money
              2. Take your money
              3. Show balance
              4. Convert to Dollar
              5. Convert to Tenge
              6. Convert to Rubl
              7. Exit""")''')
                    scan = int(input("Enter your choice "))
                    match scan:
                        case 1:
                            n = int(input("How much you want to insert "))
                            operation = USerOperations()
                            money = user.get_account()
                            sentmoney = operation.add(money, n)
                            user.set_account(sentmoney)

                        case 2:
                            n = int(input("How much you want to get "))
                            operation = USerOperations()
                            money = user.get_account()
                            sentmoney = operation.sub(money, n)
                            user.set_account(sentmoney)
                        case 3:
                            money = user.get_account()
                            currency = user.get_currency()
                            print(f"You have {money} {currency}")

                        case 4:
                            if user.get_currency() == "KZT":
                                money = user.get_account()
                                operation = USerOperations()
                                user.set_account(operation.todollar(money))
                                user.set_account_type(Account.USD.value)
                            elif user.get_currency() == "RUB":
                                money = user.get_account()
                                operation = USerOperations()
                                user.set_account(operation.fromRubl(money))
                                user.set_account_type(Account.USD.value)
                            else:
                                print("You already have USD currency")

                        case 5:
                            if user.get_currency() == "USD":
                                money = user.get_account()
                                operation = USerOperations()
                                user.set_account(operation.totenge(money))
                                user.set_account_type(Account.KZT.value)
                            elif user.get_currency() == "RUB":
                                money = user.get_account()
                                operation = USerOperations()
                                user.set_account(operation.totenge(operation.fromRubl(money)))
                                user.set_account_type(Account.KZT.value)
                            else:
                                print("You already have KZT currency")
                        case 6:
                            if user.get_currency() == "KZT":
                                money = user.get_account()
                                operation = USerOperations()
                                user.set_account(operation.toRubl(operation.todollar(money)))
                                user.set_account_type(Account.RUB.value)
                            elif user.get_currency() == "USD":
                                money = user.get_account()
                                operation = USerOperations()
                                user.set_account(operation.toRubl(money))
                                user.set_account_type(Account.RUB.value)
                            else:
                                print("You already have RUB currency")
                        case 7:
                            break
            else:
                print("User not found")

        case 0:
            print("Exited")
            break
