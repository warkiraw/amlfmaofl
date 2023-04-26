import smtplib
import random
import time
import csv
import heapq
##########################################################################################################################
class Rubeha:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.balance = 0
    #------------------------------------------------------------------------------------------------------- 
    #------------------------------------------------------------------------------------------------------- 
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
    #------------------------------------------------------------------------------------------------------- 
    #------------------------------------------------------------------------------------------------------- 
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
    #------------------------------------------------------------------------------------------------------- 
    #------------------------------------------------------------------------------------------------------- 
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
    #------------------------------------------------------------------------------------------------------- 
    #------------------------------------------------------------------------------------------------------- 
    def record_user_data(self, user_email):
        with open('users.txt', 'w') as f:
            f.write(f"{user_email} - 0")
            
    #------------------------------------------------------------------------------------------------------- 
    #------------------------------------------------------------------------------------------------------- 
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
    #------------------------------------------------------------------------------------------------------- 
    #------------------------------------------------------------------------------------------------------- 
    def account(self):
        with open("users.txt", "r") as file:
            lines = file.readlines()
            last_line = lines[-1].strip()  # get the last line and remove any trailing whitespace

        email,balance= last_line.split(" - ")
        print("Email: " + email)
        print("Balance: " + balance)
    #------------------------------------------------------------------------------------------------------- 
    #------------------------------------------------------------------------------------------------------- 
    def tickets(self):
        def read_csv_file(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                data = []
                for row in reader:
                    data.append(row)
            return data

        def create_graph(data):
            graph = {}
            for row in data:
                start, dest, price, hours = row
                price = int(price)
                hours = int(hours)
                if start not in graph:
                    graph[start] = {}
                graph[start][dest] = {'price': price, 'hours': hours}
                if dest not in graph:
                    graph[dest] = {}
                graph[dest][start] = {'price': price, 'hours': hours}
            return graph

        def shortest_path(graph, start, dest, criteria='hours'):
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            queue = [(0, start, [])]
            while queue:
                (cost, node, path) = heapq.heappop(queue)
                if node == dest:
                    path.append(node)
                    return path, distances[node]
                if path:
                    last_node = path[-1]
                else:
                    last_node = None
                if node == start or last_node in graph[node]:
                    for neighbor in graph[node]:
                        if neighbor not in path:
                            if criteria == 'hours':
                                weight = graph[node][neighbor]['hours']
                            elif criteria == 'price':
                                weight = graph[node][neighbor]['price']
                            else:
                                raise ValueError('Invalid criteria')
                            new_cost = cost + weight
                            if new_cost < distances[neighbor]:
                                distances[neighbor] = new_cost
                                new_path = path + [node]
                                heapq.heappush(queue, (new_cost, neighbor, new_path))
            return [], float('inf')

        data = read_csv_file('data.txt')
        graph = create_graph(data)
        while True:
            print("---------------------------------------------------------")
            start = input(">Начальный город:")
            print("---------------------------------------------------------")
            dest = input("?Конечный город:")
            print("---------------------------------------------------------")
            print("Для выхода нажмите 0")
            quickest_path, quickest_time = shortest_path(graph, start, dest, 'hours')
            cheapest_path, cheapest_price = shortest_path(graph, start, dest, 'price')
            print(f'Быстрейший путь от {start} до {dest}: {" -> ".join(quickest_path)}')
            print(f'Основное время: {quickest_time} часов и цена: {cheapest_price}')

            print(f'Дешевый путь от {start} до {dest}: {" -> ".join(cheapest_path)}')
            print(f'Основное время: {quickest_time} часов и цена: {cheapest_price}')
            a = input("Каким маршрутом вам будет удобнее?")
            if a=='1':
                if int(balance) > int(cheapest_price):
                    balance = int(balance) - int(cheapest_price)
                    print("Спасибо за выбор нашей компании 'Warkiraw'")
                    time.sleep(1.8)
                    print("Быстрейший маршрут находится у вас в 'Мои билеты'")
                    time.sleep(1.8)
                    print("Приятного полета")
                    time.sleep(1.8)
                    with open('users.txt', 'w') as f:
                            for line in lines:
                                if email in line:
                                    line = f"{email} - {balance}(Быстрейший путь от {start} до {dest} за {quickest_time} Часов)\n"
                                f.write(line)
                else:
                    time.sleep(1.8)
                    print("Недостаточно денег для покупки(")
                    time.sleep(1.8)
                    print("Попробуйте еще раз")
                    time.sleep(1.8)
            elif a=='2':
                if int(balance) > int(cheapest_price):
                    balance = int(balance) - int(cheapest_price)
                    print("Спасибо за выбор нашей компании 'Warkiraw'")
                    time.sleep(1.8)
                    print("Дешевый маршрут находится у вас в 'Мои билеты'")
                    time.sleep(1.8)
                    print("Приятного полета")
                    time.sleep(1.8)
                    with open('users.txt', 'w') as f:
                            for line in lines:
                                if email in line:
                                    line = f"{email} - {balance}(Самый дешевый путь от {start} до {dest} за {quickest_time} тенге)\n"
                                f.write(line)
                else:
                    time.sleep(1.8)
                    print("Недостаточно денег для покупки(")
                    time.sleep(1.8)
                    print("Попробуйте еще раз")
                    time.sleep(1.8)
            else:
                break
    #------------------------------------------------------------------------------------------------------- 
    #------------------------------------------------------------------------------------------------------- 
    def my_tickets(self):
        with open("users.txt", "r") as file:
            lines = file.readlines()
            last_line = lines[-1].strip()

            # split the string by dash and extract the balance value
            email, balance, *tickets = last_line.split(" - ")
            balance = int(balance.split("(")[0])

            print(email)
            print(balance)
            print(tickets)


##########################################################################################################################
x = Rubeha('warkirawcik@gmail.com', 'kmtkxxvwmtgbuuvn')
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
        c = print(">Выход")
        a = print("----------------------------------------------------")
    main()
    c = input("Выберите действие:")
    a = print("----------------------------------------------------")
    with open("users.txt", "r") as file:
        lines = file.readlines()
        last_line = lines[-1].strip()  # get the last line and remove any trailing whitespace

    email,balance= last_line.split(" - ")
    balance = int(balance.split("(")[0])
    if c=="1":
        x.account()
        time.sleep(3)
    elif c=="2":
        x.update_balance(email)
        time.sleep(3)
    elif c=="3":
        while True:
            def end():
                a = print("----------------------------------------------------")
                b = print(">Купить билеты")
                a = print("----------------------------------------------------")
                c = print(">Мои билеты")
                a = print("----------------------------------------------------")
                b = print(">Выход")
                a = print("----------------------------------------------------")
            end()
            r = input("Выберите действие:")
            a = print("----------------------------------------------------")
            time.sleep(2)
            if r=='1':
                x.tickets()
                time.sleep(3)
            elif r=='2':
                x.my_tickets()
                time.sleep(3)
            elif r=='3':
                break
    elif c=="4":
        break
