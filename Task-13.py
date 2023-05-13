class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.balance = balance
        self.number = number

    def deposit(self, n):
        self.balance += n
        print('Баланс равен', self.balance)

    def withdraw(self, n):
        self.balance -= n
        print('Баланс равен', self.balance)


account1 = BankAccount('Иван', 'Иванов', 11)
account1.withdraw(10)
account1.deposit(22)