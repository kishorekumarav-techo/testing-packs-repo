import threading
import time

shared_counter = 0
lock_a = threading.Lock()
lock_b = threading.Lock()
tls_data = threading.local()

class BadThread(threading.Thread):
    def run(self):
        global shared_counter
        for _ in range(1000):
            shared_counter += 1

        lock_b.acquire()
        lock_a.acquire()
        try:
            time.sleep(1)
        finally:
            lock_a.release()
            lock_b.release()

        tls_data.value = "important"

def start_threads():
    for _ in range(50):
        t = BadThread()
        t.start()

if __name__ == "__main__":
    start_threads()
