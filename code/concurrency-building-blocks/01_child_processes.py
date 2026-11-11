"""
Spawning child processes.

Demonstrates how a parent process can create multiple child processes
using Python's multiprocessing module. Each child runs independently
with its own PID and memory space.
"""

import os
from multiprocessing import Process


def run_child() -> None:
    print(f"Child: PID={os.getpid()}, Parent PID={os.getppid()}")


def main():
    print(f"Parent: PID={os.getpid()}")
    for _ in range(3):
        process = Process(target=run_child)
        process.start()


if __name__ == "__main__":
    main()
