"""
Pipe IPC: writer and reader threads.

Demonstrates how two threads can communicate through an unnamed pipe.
The writer sends a message through one end of the pipe, and the
reader receives it from the other end.
"""

from threading import Thread, current_thread
from multiprocessing import Pipe
from multiprocessing.connection import Connection


class Writer(Thread):
    def __init__(self, conn: Connection):
        super().__init__()
        self.conn = conn

    def run(self) -> None:
        print(f"{current_thread().name}: Sending rubber duck...")
        self.conn.send("Rubber duck")


class Reader(Thread):
    def __init__(self, conn: Connection):
        super().__init__()
        self.conn = conn

    def run(self) -> None:
        msg = self.conn.recv()
        print(f"{current_thread().name}: Received: {msg}")


def main():
    reader_conn, writer_conn = Pipe()
    writer = Writer(writer_conn)
    reader = Reader(reader_conn)
    writer.start()
    reader.start()
    writer.join()
    reader.join()


if __name__ == "__main__":
    main()
