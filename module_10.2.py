import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self, enemy = 100):
        print(f"{self.name}, we're under attack!")
        day = 0
        while enemy:
            day += 1
            enemy -= self.power
            time.sleep(1)
            print(f'{self.name} fights for {day} days, {enemy} enemies remain!')
        print(f'{self.name} vanquished all foes in {day} days!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()


