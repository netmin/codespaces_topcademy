import threading


def hello_from_thread():
    print(f'hello from thread {threading.current_thread()}!')


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()
total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python execute {total_threads} threads')
print(f'Thread name {thread_name}')

hello_thread.join()


if __name__ == "__main__":
    hello_from_thread()