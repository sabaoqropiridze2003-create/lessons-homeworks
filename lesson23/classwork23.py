import asyncio
import time


tasks = [
    ("Downloading data", 3),
    ("Processing data", 2),
    ("Sending notification", 1),
    ("Saving results", 4),
]


async def run_task(name, duration):
    print(f"Started: {name}")
    await asyncio.sleep(duration)
    print(f"Finished: {name}")
    return f"{name} completed successfully"


async def run_sequential():
    print("--- Sequential---")
    start_time = time.perf_counter()

    for name, duration in tasks:
        await run_task(name, duration)

    end_time = time.perf_counter()
    return end_time - start_time


async def run_concurrent():
    print("--- Concurrent---")
    start_time = time.perf_counter()

    task_coroutines = [run_task(name, duration) for name, duration in tasks]
    await asyncio.gather(*task_coroutines)

    end_time = time.perf_counter()
    return end_time - start_time


async def main():
    sequential_time = await run_sequential()
    print()

    concurrent_time = await run_concurrent()
    print()

    print(f"Sequential time: {sequential_time:.2f} seconds")
    print(f"Concurrent time: {concurrent_time:.2f} seconds")

asyncio.run(main())
