from typing import Union
import sys

class Bank:
    def __init__(self) -> None:
        self.account_data = {}
        self.card_data = {}

    def add_account(self, card, account, balance) -> None:
        if card not in self.account_data.keys():
            self.account_data[card] = {account: balance}
        else:
            self.account_data[card][account] = balance

    def add_card(self, card, pin) -> None:
        self.card_data[card] = {'pin':pin, 'account': self.account_data[card]}

    def valid_card(self, card) -> bool:
        print(f'Card name is {card}')
        if card in self.card_data.keys():
            return True
        else:
            return False

    def valid_pin(self, card, pin) -> bool:
        if pin == self.card_data[card]['pin']:
            return True
        else:
            return False

    def see_balance(self, card, user_account) -> int:
        return self.account_data[card][user_account]

    def deposit(self, card, user_account, money) -> int:
        if money > 0:
            self.account_data[card][user_account] += money
            return self.account_data[card][user_account]
        else:
            print('Please deposit more than 1 dollor')
            return self.account_data[card][user_account]

    def withdraw(self, card, user_account, money) -> int:
        if money <= 0:
            print('Please withdraw more than 1 dollor')
            return self.account_data[card][user_account] 

        if self.account_data[card][user_account] >= money:
            self.account_data[card][user_account] -= money
            return self.account_data[card][user_account]
        else:
            print('You cannot withdraw more than your balance of account.')
            return self.account_data[card][user_account]


class ATM:
    def __init__(self) -> None:
        pass

    def print_action() -> None:
        print('*'*50)
        print('[1] See Balance')
        print('[2] Deposit')
        print('[3] Withdraw')
        print('[4] Change Account')
        print('[5] Exit')
        print('*'*50)

    def print_couninue() -> str:
        add_action = input('Continue? If yes, enter Y : ')
        return add_action

    def insert_card(base) -> Union[str, bool]:
        card = input('Insert card : ')
        if base.valid_card(card):
            return card
        else:
            return False

    def insert_pin(card, base) -> Union[str, bool]:
        pin = int(input('Insert PIN : '))
        if base.valid_pin(card, pin):
            return True
        else:
            return False

    def select_account(card, base) -> str:
        accounts = {}
        print('number \taccount'.expandtabs())
        for idx, val in enumerate(base.account_data[card].keys()):
            print(f'[{idx}]\t{val}'.expandtabs())
            accounts[idx] = val
        
        while True:
            n = int(input('Select number : '))
            if n in accounts.keys():
                break
            else:
                continue
            
        return accounts[n]
        
    def print_balance(card, user_account, base) -> None:
        amount = base.see_balance(card, user_account)
        print(f'The total amount of {user_account} account is {amount}')

    def print_deposit(card, user_account, money, base) -> None:
        amount = base.deposit(card, user_account, money)
        print(f'The total amount of {user_account} account is {amount}')

    def print_withdrawal(card, user_account, money, base) -> None:
        amount = base.withdraw(card, user_account, money)
        print(f'The total amount of {user_account} account is {amount}')


def main():
    # Add account, card and PIN
    base = Bank()
    base.add_account('bisa', 'A_bank_account', 1000)
    base.add_account('bisa', 'B_bank_account', 2000)
    base.add_card('bisa', 1234)
    
    # print(base.card_data)
    # print(base.account_data)
    
    valid_card, valid_pin = False, False
    while True:
        card = ATM.insert_card(base)    # Check card
        if card:
            valid_card = True
            pin_count = 0
            while pin_count < 5:
                pin = ATM.insert_pin(card, base)  # Check PIN 
                if pin:
                    valid_pin = True
                    user_account = ATM.select_account(card, base) # select account
                    break
                else:
                    print(f'You try {pin_count+1} time. If you fail more than 5 times, you must re-insert the card.')
                    pin_count += 1
                    exit = input('Do you want to exit? then enter Y : ')
                    if exit == 'Y':
                        sys.exit()

        if not card:
            exit = input('Please insert a correct card. Do you want to exit? then enter Y : ')
            if exit == 'Y':
                sys.exit()

        if valid_card and valid_pin:
            break
    
    if valid_card and valid_pin:
        while True:
            print(f'Your account is {user_account}')
            ATM.print_action()
            key = int(input('Enter number. : '))

            if key == 1: # See balance
                ATM.print_balance(card, user_account, base)
                add_action = ATM.print_couninue()
                if add_action == 'Y':
                    continue
                else:
                    break

            elif key == 2: # Deposit
                money = int(input('Enter the amount you want to save. : '))
                ATM.print_deposit(card, user_account, money, base)
                add_action = ATM.print_couninue()
                if add_action == 'Y':
                    continue
                else:
                    break

            elif key == 3: # Withdraw
                money = int(input('Enter the amount you want to withdraw. : '))
                ATM.print_withdrawal(card, user_account, money, base)
                add_action = ATM.print_couninue()
                if add_action == 'Y':
                    continue
                else:
                    break

            elif key == 4: # Change account
                 user_account = ATM.select_account(card, base) # select account

            elif key == 5: # Quit
                break

            else:
                print('Please enter a correct number')
                continue
    

if __name__ == "__main__":
    main()
