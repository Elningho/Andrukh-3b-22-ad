class Bank:
    def __init__(self):
        self.clients = {}

    def create_client(self, client_id, name):
        if client_id not in self.clients:
            self.clients[client_id] = {"name": name, "accounts": {}}
            print(f'Клиент {name} с ID {client_id} успешно создан.')
        else:
            print(f'Ошибка: Клиент с ID {client_id} уже существует.')

    def open_account(self, client_id, account_id, initial_balance=0):
        if client_id in self.clients:
            if account_id not in self.clients[client_id]["accounts"]:
                if initial_balance >= 0:
                    self.clients[client_id]["accounts"][account_id] = initial_balance
                    print(f'Счет {account_id} успешно открыт для клиента {self.clients[client_id]["name"]}.')
                else:
                    print('Ошибка: Начальный баланс не может быть отрицательным.')
            else:
                print(f'Ошибка: Счет с ID {account_id} уже существует для клиента {self.clients[client_id]["name"]}.')
        else:
            print(f'Ошибка: Клиент с ID {client_id} не существует.')

    def transfer_funds(self, sender_client_id, sender_account_id, recipient_client_id, recipient_account_id, amount):
        if sender_client_id in self.clients and recipient_client_id in self.clients:
            sender_accounts = self.clients[sender_client_id]["accounts"]
            recipient_accounts = self.clients[recipient_client_id]["accounts"]

            if sender_account_id in sender_accounts and recipient_account_id in recipient_accounts:
                sender_balance = sender_accounts[sender_account_id]
                recipient_balance = recipient_accounts[recipient_account_id]

                if sender_balance >= amount:
                    sender_accounts[sender_account_id] -= amount
                    recipient_accounts[recipient_account_id] += amount
                    print(f'Перевод {amount} рублей со счета {sender_account_id} на счет {recipient_account_id} успешно выполнен.')
                else:
                    print('Ошибка: Недостаточно средств на счете отправителя.')
            else:
                print('Ошибка: Некорректный ID счета отправителя или получателя.')
        else:
            print('Ошибка: Некорректный ID клиента отправителя или получателя.')


bank = Bank()

bank.create_client('123', 'Иванов Иван Иванович')
bank.create_client('456', 'Сидоров Сидор Сидорович')

bank.open_account('123', '1111', 1000)
bank.open_account('123', '2222', 500)

bank.open_account('456', '3333', 2000)

bank.transfer_funds('123', '1111', '456', '3333', 500)
bank.transfer_funds('123', '2222', '456', '3333', 1000)
