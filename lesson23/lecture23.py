import time
import asyncio


# def task1():
#     print("task 1 started")
#     time.sleep(3)
#     print("task 1 ended")

# print(task1())

# async def task1():
#     print("task 1 started")
#     time.sleep(3)
#     return "task 1 ended"

# result = asyncio.run(task1())

# print(result)


# async def task1():
#     print("task 1 started")
#     await asyncio.sleep(3)
#     print("task 1 ended")


# async def task2():
#     print("task 2 started")
#     await asyncio.sleep(2)
#     print("task 2 ended")


# async def main():

#     start_time = time.perf_counter()

#     t1 = asyncio.create_task(task1())
#     t2 = asyncio.create_task(task2())

#     await t1
#     await t2

#     print(f"total time: {time.perf_counter() - start_time:.2f}")

# asyncio.run(main())

# async def main():
#     results = await asyncio.gather(task1(), task2())


# asyncio.run(main())

# async def task1():
#     print("task 1 started")
#     await asyncio.sleep(3)
#     return "task 1 ended"


# async def task2():
#     print("task 2 started")
#     await asyncio.sleep(2)
#     return "task 2 ended"


# async def main():
#     results = await asyncio.gather(task1(), task2())
#     print(results)

# asyncio.run(main())


# async def davaleba(name):
#     print(f"Task {name} started")
#     await asyncio.sleep(1)
#     print(f"task {name} ended")


# async def main():

#     start = time.perf_counter()
#     tasks = []

#     for i in range(1, 6):
#         tasks.append(asyncio.create_task(davaleba(i)))

#     for task in tasks:
#         await task

#     end = time.perf_counter()

#     print(f"Total time {end - start:.2f}")

# asyncio.run(main())


# async def davaleba(name):
#     print(f"Task {name} started")
#     await asyncio.sleep(1)
#     print(f"task {name} ended")


# async def main():

#     start = time.perf_counter()
#     # tasks = []

#     # for i in range(1, 6):
#     #     tasks.append(davaleba(i))

#     tasks = [davaleba(i) for i in range(1, 6)]

#     await asyncio.gather(*tasks)
#     end = time.perf_counter()

#     print(f"Total time {end - start:.2f}")

# asyncio.run(main())
