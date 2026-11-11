"""
Shared-memory IPC: producer/consumer pattern.

Demonstrates how two threads can communicate through a shared array.
The producer writes values into the array, and the consumer reads
them. The consumer polls until data becomes available.
"""

import time
from threading import Thread

SIZE = 5
shared_memory = [-1] * SIZE


class Producer(Thread):
    def run(self) -> None:
        for i in range(SIZE):
            print(f"Producer: Writing {i}")
            shared_memory[i] = i


class Consumer(Thread):
    def run(self) -> None:
        for i in range(SIZE):
            while shared_memory[i] == -1:
                time.sleep(0.5)
            print(f"Consumer: Read {shared_memory[i]}")


def main():
    consumer = Consumer()
    producer = Producer()
    consumer.start()
    producer.start()
    consumer.join()
    producer.join()


if __name__ == "__main__":
    main()
