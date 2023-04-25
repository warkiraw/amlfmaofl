import smtplib
import random
import time
import csv

class EmailVerifier:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.balance = 0
        
    def generate_verification_code(self):
        return random.randint(100000, 999999)
    
    def send_verification_code(self, user_email, verification_code):
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.email, self.password)
            subject = 'Рубежка по Питону'
            message = f"Привет,вот твой проверочный код: \n\n{verification_code}"
            message = f"Subject: {subject}\n\n{message}\n\nGood Luck,Have Fun"
            message = message.encode('utf-8')
            server.sendmail(self.email, user_email, message)
    
    def verify_email(self,user_email):
        verification_code = self.generate_verification_code()
        self.send_verification_code(user_email, verification_code)
        while True:
            user_code = input("Введите код,который мы отправили вам на почту: ")
            print("----------------------------------------------------")
            if int(user_code) == verification_code:
                print("Верификация прошла успешно.Можешь идти).")
                print("----------------------------------------------------")
                self.record_user_data(user_email)
                time.sleep(3)
                break
            else:
                print("Чтото пошло не так.Попробуй еще раз")
                print("----------------------------------------------------")
    def update_balance(self,user_email):
        print('Ваш баланс равен:' + str(self.balance))
        print("----------------------------------------------------")
        amount = int(input("Введите сумму для пополнения баланса: "))
        self.balance += amount
        print("----------------------------------------------------")
        print('Баланс был пополнен на сумму:' + str(amount))
        print("----------------------------------------------------")
        print('Ваш баланс равен:' + str(self.balance))
        with open('users.txt', 'r') as f:
            lines = f.readlines()
    
        with open('users.txt', 'w') as f:
            for line in lines:
                if user_email in line:
                    line = f"{user_email} - {self.balance}\n"
                f.write(line)

    
    def record_user_data(self, user_email):
        with open('users.txt', 'r+') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if user_email in line:
                    # Update the balance of the user
                    balance = int(line.split('-')[1].strip())
                    lines[i] = f"{user_email} - {balance}\n"
                    break
            else:
                # Add a new line for the user with zero balance
                lines.append(f"{user_email} - 0\n")

            # Move the file pointer to the beginning of the file
            f.seek(0)
            # Write the modified lines back to the file
            f.writelines(lines)
            # Truncate the remaining content of the file (if any)
            f.truncate()
    def check_email(self):
        user_email = input("Введите свою почту: ")
        print("----------------------------------------------------")
        with open('users.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if user_email in line:
                    print("Данный email уже зарегестрирован,зайдите через вход")
                else:
                    x.verify_email(user_email)
    def account(self):
        with open("users.txt", "r") as file:
            lines = file.readlines()
            last_line = lines[-1].strip()  # get the last line and remove any trailing whitespace

        email,balance= last_line.split(" - ")
        print("Email: " + email)
        print("Balance: " + balance)
    def tickets(self):
        print ("You good bitches!")
x = EmailVerifier('warkirawcik@gmail.com', 'kmtkxxvwmtgbuuvn')
def start():
        a = print("----------------------------------------------------")
        b = print(">Вход")
        a = print("----------------------------------------------------")
        c = print(">Регистрация")
        a = print("----------------------------------------------------")
start()
a = input("Выберите действие:")
print("----------------------------------------------------")
if a =='1':
    z = input("Укажите email который указывали при регистрации:")
    a = print("----------------------------------------------------")
    x.verify_email(z)
    time.sleep(3)
elif a =='2':
    x.check_email()
while True:
    def main():
        a = print("----------------------------------------------------")
        b = print(">Личный кабинет")
        a = print("----------------------------------------------------")
        c = print(">Пополнение баланса")
        a = print("----------------------------------------------------")
        b = print(">Туры")
        a = print("----------------------------------------------------")
        b = print(">Сменить аккаунт")
        a = print("----------------------------------------------------")
        c = print(">Выход")
        a = print("----------------------------------------------------")
    main()
    c = input("Выберите действие:")
    a = print("----------------------------------------------------")
    with open("users.txt", "r") as file:
        lines = file.readlines()
        last_line = lines[-1].strip()  # get the last line and remove any trailing whitespace

    email,balance= last_line.split(" - ")
    if c=="1":
        x.account()
        time.sleep(3)
    elif c=="2":
        x.update_balance(email)
        time.sleep(3)
    elif c=="3":
        x.tickets()
        time.sleep(3)
    elif c=="4":
        start()
    elif c=="5":
        break