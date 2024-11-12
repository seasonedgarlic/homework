import threading
from queue import Queue
import time
import random

class Table:
    def __init__(self, number):
        self.number = int(number)
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = str(name)
    def run(self):
        delay = random.randint(3, 10)
        time.sleep(delay)

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)
    def guest_arrival(self, *guests):
        for guest in guests:
            available_table = next((table for table in self.tables if table.guest is None), None)
            if available_table:
                available_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {available_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                guest = table.guest
                if guest and not guest.is_alive():
                    print(f"{guest.name} покушал(-а) и ушёл(-ла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            time.sleep(1)


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()