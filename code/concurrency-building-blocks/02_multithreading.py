"""
Creating multiple threads.

Demonstrates how to create and run multiple threads within a single
process. All threads share the same PID but execute independently.
"""

import threading
from threading import Thread


def do_work(task_id: int) -> None:
    name = threading.current_thread().getName()
    print(f"{name} is handling task {task_id}")


def main():
    threads = []
    for i in range(5):
        thread = Thread(target=do_work, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
