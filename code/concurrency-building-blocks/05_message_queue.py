"""
Message queue IPC: multiple workers processing a shared queue.

Demonstrates how multiple worker threads can consume tasks from a
shared message queue. Each worker picks up the next available item
and processes it independently.
"""

import time
from queue import Queue
from threading import Thread, current_thread


class Worker(Thread):
    def __init__(self, queue: Queue, id: int):
        super().__init__(name=str(id))
        self.queue = queue

    def run(self) -> None:
        while not self.queue.empty():
            item = self.queue.get()
            print(f"Thread {current_thread().name}: "
                  f"processing item {item}")
            time.sleep(1)


def main():
    q = Queue()
    for i in range(10):
        q.put(i)

    threads = []
    for i in range(4):
        thread = Worker(q, i + 1)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
