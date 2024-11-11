import threading
import random
import time

class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            depo = random.randint(50, 500)
            self.balance += depo
            print(f'Пополнение: {depo}, текущий баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                time.sleep(0.001)

    def take(self):
        for i in range(100):
            tax = random.randint(50, 500)
            print(f'Запрос на {tax}')
            if tax <= self.balance:
                self.balance - tax
                print(f'Снятие: {tax}, баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')