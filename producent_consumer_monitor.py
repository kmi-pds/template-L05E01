import random
import time
import string
from threading import Thread, Condition, Lock


class MonitorPC:
    def __init__(self, buffer_size):
        self.buffer = [None] * buffer_size
    
    def put(self, item):
        pass
    
    def get(self):
        pass


def produce():
    item = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    print(f"Produced: {item}")
    return item


def consume(item):
    print(monitor.buffer)
    print(f"Consumed: {item}")


def producent():
    while loop_forever:
        time.sleep(random.randint(0, 4))
        item = produce()
        monitor.put(item)


def consumer():
    while loop_forever:
        time.sleep(random.randint(0, 4))
        item = monitor.get()
        consume(item)

    
if __name__ == "__main__":
    monitor = MonitorPC(random.randint(5, 10))
    loop_forever = True

    producent_thread = Thread(target=producent)
    consumer_thread = Thread(target=consumer)

    producent_thread.start()
    consumer_thread.start()

    time.sleep(15)

    loop_forever = False

    producent_thread.join()
    consumer_thread.join()