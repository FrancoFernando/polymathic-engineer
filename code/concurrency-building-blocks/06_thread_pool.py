"""
Thread pool pattern.

Demonstrates a basic thread pool implementation. Worker threads are
created once at startup and reused to process tasks from a shared
queue, avoiding the overhead of creating a new thread for each task.
"""

import time
import queue
from threading import Thread, current_thread


class Worker(Thread):
    def __init__(self, tasks: queue.Queue):
        super().__init__()
        self.tasks = tasks

    def run(self) -> None:
        while True:
            func, args, kwargs = self.tasks.get()
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(e)
            self.tasks.task_done()


class ThreadPool:
    def __init__(self, num_threads: int):
        self.tasks = queue.Queue(num_threads)
        for _ in range(num_threads):
            worker = Worker(self.tasks)
            worker.setDaemon(True)
            worker.start()

    def submit(self, func, *args, **kwargs) -> None:
        self.tasks.put((func, args, kwargs))

    def wait_completion(self) -> None:
        self.tasks.join()


def do_work(i: int) -> None:
    name = current_thread().getName()
    print(f"{name} doing {i} work")
    time.sleep(2)


def main():
    pool = ThreadPool(num_threads=5)
    for i in range(20):
        pool.submit(do_work, i)

    print("All work requests sent")
    pool.wait_completion()
    print("All work completed")


if __name__ == "__main__":
    main()
