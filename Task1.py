from queue import Queue
import time

queue = Queue()
request_id = 0


def generate_request():
    global request_id
    request_id += 1
    request = f"Request #{request_id}"
    queue.put(request)
    print(f"Створено: {request}")


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробляю: {request}")
    else:
        print("Черга пуста")


for _ in range(5):
    generate_request()
    process_request()
