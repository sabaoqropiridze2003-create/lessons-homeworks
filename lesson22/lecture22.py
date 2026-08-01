import os
import time
import threading
import multiprocessing


def page_load(url):
    print(f"[Page Load Started] {url}")
    time.sleep(2)
    print(f"[page loaded] {url}")


# start = time.time()

# page_load("youtube.com")
# page_load("google.com")
# page_load("gmail.com")

# end = time.time()
# print(f"{end - start:.2f} seconds")

# print("=======" * 10)


# thrd1 = threading.Thread(target=page_load, args=("youtube.com",))
# thrd2 = threading.Thread(target=page_load, args=("google.com",))
# thrd3 = threading.Thread(target=page_load, args=("gmail.com",))

# start = time.time()

# print(f"\n {threading.enumerate()}")
# print(f"{threading.active_count()} - threads number")

# thrd1.start()
# thrd2.start()
# thrd3.start()

# print(f"\n {threading.enumerate()}")
# print(f"{threading.active_count()} - threads number")

# thrd1.join()
# thrd2.join()
# thrd3.join()

# print(f"\n {threading.enumerate()}")
# print(f"{threading.active_count()} - threads number")

# end = time.time()
# print(f"{end - start:.2f} seconds")


# thrd1 = threading.Thread(target=page_load, args=("youtube.com",))
# thrd2 = threading.Thread(target=page_load, args=("google.com",))
# thrd3 = threading.Thread(target=page_load, args=("gmail.com",))

# start = time.time()


# thrd1.start()
# thrd2.start()
# thrd3.start()

# # print("main thread ended")


# thrd1.join()
# thrd2.join()
# thrd3.join()

# print("main thread ended")


# end = time.time()
# print(f"{end - start:.2f} seconds")

# def download_page(url):
#     thread_name = threading.current_thread().name
#     print(f"[{thread_name}] დაიწყო: {url}")
#     time.sleep(2)
#     print(f"[{thread_name}] დასრულდა: {url}")


# urls = [
#     "google.com",
#     "facebook.com",
#     "github.com",
#     "python.org",
#     "stackoverflow.com",
# ]

# threads = []

# start = time.time()

# for i in urls:
#     t = threading.Thread(target=download_page, args=(i,))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# end = time.time()
# print(f"{end-start:.2f}")

# room_is_free = True

# lock = threading.Lock()


# def book_room(client_name):
#     global room_is_free

#     print(f"{client_name} is checking room status")

#     with lock:

#         if room_is_free:
#             print(
#                 f"{client_name} saw that room is free so he startet filling the papers")

#             time.sleep(1)

#             room_is_free = False

#             print(f"{client_name} sucsesfully booked a room")
#         else:
#             print(f"{client_name} room is already taken")


# t1 = threading.Thread(target=book_room, args=("saba",))
# t2 = threading.Thread(target=book_room, args=("giorgi",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# def heavy_task(n):
#     total = 0
#     for i in range(n):
#         total += 1 * 1


# big_n = 30_000_000

# start = time.time()

# heavy_task(big_n)
# heavy_task(big_n)

# end = time.time()

# print(f"{end - start:.2f} seconds for tanmimdevruli")


# start = time.time()

# t1 = threading.Thread(target=heavy_task, args=(big_n,))
# t2 = threading.Thread(target=heavy_task, args=(big_n,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# end = time.time()

# print(f"{end - start:.2f} seconds for threads")


# def heavy_task(n):
#     total = 0
#     for i in range(n):
#         total += 1 * 1


# big_n = 60_000_000


# if __name__ == '__main__':
#     start = time.time()

#     heavy_task(big_n)
#     heavy_task(big_n)

#     end = time.time()
#     print(f"{end - start:.2f} seconds for tanmimdevruli")

#     start = time.time()

#     p1 = multiprocessing.Process(target=heavy_task, args=(big_n,))
#     p2 = multiprocessing.Process(target=heavy_task, args=(big_n,))

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#     end = time.time()
#     print(f"{end - start:.2f} seconds for multiprocesing")


# def producer(queue, items):

#     for item in items:
#         print(f"[Producer] adding {item}")
#         queue.put(item)
#         time.sleep(0.5)
#     queue.put(None)


# def consumer(queue):

#     while True:
#         item = queue.get()
#         if item is None:
#             print("[consumer] ended")
#             break
#         print(f"[consumer] procesing {item}")
#         time.sleep(1)


# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
#     items = ["file1", "file2", "file3", "file4"]

#     p1 = multiprocessing.Process(target=producer, args=(queue, items))
#     p2 = multiprocessing.Process(target=consumer, args=(queue,))

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


def process_file(filename):
    pid = os.getpid()
    print(f"[PID {pid}] procesing {filename}")

    total = sum(i * i for i in range(5_000_000))

    print(f"[PID {pid}] ended {filename}")


if __name__ == "__main__":

    files = ["file_1", "file_2", "file_3", "file_4", "file_5"]

    start = time.time()
    with multiprocessing.Pool(processes=3) as pool:
        pool.results = pool.map(process_file, files)

    end = time.time()
    print(f"end time is {end - start:.2f}")
