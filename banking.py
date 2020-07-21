# Write your code here
import random
import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
conn.commit()


class BankingSystem:
    current_card_number = None
    current_balance = None
    option = None

    def logged_out(self):
        print("""1. Create an account
2. Log into account
0. Exit""")

    def create_card(self):
        card_number = None
        check = 0
        random_choice = 0
        while not card_number or cur.fetchone():
            listed_sequence = random.sample(range(10), 9)
            card_number = "400000"\
                          + "".join(str(listed_sequence[i]) for i in range(9))
            for i in range(0, 15, 2):
                check_multiply = int(card_number[i]) * 2
                if check_multiply > 9:
                    check = check + check_multiply - 9
                else:
                    check = check + check_multiply
            for i in range(1, 15, 2):
                check = check + int(card_number[i])
            while (check + random_choice) % 10 != 0:
                random_choice = random.choice(range(10))
            card_number = card_number + str(random_choice)
            listed_sequence = random.sample(range(10), 4)
            pin_code = "".join(str(listed_sequence[i]) for i in range(4))
            card_id = random.choice(range(3000000))
            cur.execute('''SELECT id FROM card
            WHERE 
            id = {}
            AND number = {}'''.format(card_id,
                                      card_number))
        cur.execute('''INSERT INTO card (id, number, pin)
VALUES ({}, {}, {})'''.format(card_id,
                              card_number,
                              pin_code))
        conn.commit()
        print("""Your card has been created
Your card number:
{}
Your card PIN:
{}""".format(card_number, pin_code))

    def log_into_account(self, card_number, pin_code):
        cur.execute('''SELECT
         id 
         FROM
         card 
         WHERE
         number = {}
         AND pin = {}'''.format(card_number,
                                pin_code))
        if cur.fetchone():
            cur.execute('''SELECT balance FROM card WHERE
number = {}'''.format(card_number))
            self.current_balance = int(cur.fetchone()[0])
            self.current_card_number = card_number
            print("You have successfully logged in!")
        else:
            print("Wrong card number or PIN!")

    def add_income(self, income_value):
        cur.execute('''UPDATE card
         SET balance = balance + {}
         WHERE number = {}'''.format(int(income_value),
                                     self.current_card_number))
        conn.commit()
        self.current_balance += int(income_value)
        print("Income was added!")

    def transfer(self, card_number):
        cur.execute('''SELECT
        number
        FROM
        card
        WHERE
        number = {}'''.format(card_number))
        check = 0
        for i in range(0, 15, 2):
            check_multiply = int(card_number[i]) * 2
            if check_multiply > 9:
                check = check + check_multiply - 9
            else:
                check = check + check_multiply
        for i in range(1, 15, 2):
            check = check + int(card_number[i])
        check = check + int(card_number[15])
        if check % 10 != 0:
            print("Probably you made mistake in the card number. Please try again!")
        elif not cur.fetchone():
            print("Such a card does not exist.")
        elif self.current_card_number == card_number:
            print("You can't transfer money to the same account!")
        else:
            transfer_value = int(input("Enter how much money you "
                                       "want to transfer:"))
            if self.current_balance < transfer_value:
                print("Not enough money!")
            else:
                cur.execute('''UPDATE card
                SET balance = balance + {}
                WHERE number = {}'''.format(transfer_value,
                                            card_number))
                conn.commit()
                cur.execute('''UPDATE card
                SET balance = balance - {}
                WHERE number = {}'''.format(transfer_value,
                                            self.current_card_number))
                conn.commit()
                self.current_balance -= transfer_value
                print("Success!")

    def close_account(self):
        cur.execute('''DELETE FROM
         card 
         WHERE
          number = {}'''.format(self.current_card_number))
        conn.commit()
        self.current_card_number = None
        self.current_balance = None
        print("The account has been closed!")

    def logged_in(self):
        print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")

    def log_out(self):
        self.current_card_number = None
        self.current_balance = None

    def option_reader(self, option):
        self.option = option

    def exit(self):
        print("Bye!")


bank = BankingSystem()


while True:
    if not bank.current_card_number:
        bank.logged_out()
        bank.option_reader = int(input())
        if bank.option_reader == 1:
            bank.create_card()
        elif bank.option_reader == 2:
            bank.log_into_account(input("Enter your card number:"),
                                  input("Enter your PIN:"))
        else:
            bank.exit()
            break
    else:
        bank.logged_in()
        bank.option_reader = int(input())
        if bank.option_reader == 1:
            print("Balance: " + str(bank.current_balance))
        elif bank.option_reader == 2:
            bank.add_income(int(input("Enter income:")))
        elif bank.option_reader == 3:
            bank.transfer(input("Enter card number:"))
        elif bank.option_reader == 4:
            bank.close_account()
        elif bank.option_reader == 5:
            bank.log_out()
        else:
            bank.exit()
            break
