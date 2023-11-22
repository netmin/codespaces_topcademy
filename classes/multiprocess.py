from multiprocessing import Process
import os


def hello_from_process():
    print(f'hello from child process {os.getpid()}!')


if __name__ == '__main__':
    hello_process = Process(target=hello_from_process)
    hello_process.start()
    print(f'parent process {os.getpid()}')
    hello_process.join()