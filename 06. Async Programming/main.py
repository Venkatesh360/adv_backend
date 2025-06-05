import asyncio
from time import perf_counter
from colorama import Fore, init

init(autoreset=True)


async def function(task_name: str) -> None:
    """
    Simulates an asynchronous task with a 2-second delay.

    Args:
        task_name (str): The name of the task.
    """
    print(Fore.YELLOW + f"  ↪ Starting: {task_name}")
    await asyncio.sleep(2.0)
    print(Fore.GREEN + f"  ✔ Finished: {task_name}")


async def concurrent() -> None:
    """
    Runs async tasks one after another (sequentially).
    """
    print(Fore.RED + "▶ Running in CONCURRENT (sequential) mode")
    print("=" * 50)
    start = perf_counter()

    tasks = ["Organize stuff", "Do laundry", "Clean my room"]
    for task in tasks:
        await function(task)

    end = round(perf_counter() - start, 2)
    print("=" * 50)
    print(Fore.BLUE + f"⏱ Total time taken: {end} seconds")
    print("=" * 50)


async def parallel_with_task_groups() -> None:
    """
    Runs async tasks concurrently using TaskGroup (Python 3.11+).
    """
    print(Fore.RED + "▶ Running in PARALLEL mode (TaskGroup)")
    print("=" * 50)
    start = perf_counter()

    tasks = ["Organize stuff", "Do laundry", "Clean my room"]

    async with asyncio.TaskGroup() as tg:
        for task in tasks:
            tg.create_task(function(task))

    end = round(perf_counter() - start, 2)
    print("=" * 50)
    print(Fore.BLUE + f"⏱ Total time taken: {end} seconds")
    print("=" * 50)


async def parallel_with_create_tasks() -> None:
    """
    Runs async tasks concurrently using create_task() and asyncio.wait().
    """
    print(Fore.RED + "▶ Running in PARALLEL mode (create_task + wait)")
    print("=" * 50)
    start = perf_counter()

    tasks = ["Organize stuff", "Do laundry", "Clean my room"]
    async_tasks = [asyncio.create_task(function(task)) for task in tasks]
    done, pending = await asyncio.wait(async_tasks, timeout=3)

    end = round(perf_counter() - start, 2)
    print("=" * 50)
    print(Fore.BLUE + f"⏱ Total time taken: {end} seconds")
    print("=" * 50)


async def parallel_with_gather() -> None:
    """
    Runs async tasks concurrently using asyncio.gather().
    """
    print(Fore.RED + "▶ Running in PARALLEL mode (asyncio.gather)")
    print("=" * 50)
    start = perf_counter()

    tasks = ["Organize stuff", "Do laundry", "Clean my room"]
    async_tasks = [function(task) for task in tasks]
    await asyncio.gather(*async_tasks, return_exceptions=True)

    end = round(perf_counter() - start, 2)
    print("=" * 50)
    print(Fore.BLUE + f"⏱ Total time taken: {end} seconds")
    print("=" * 50)


async def main() -> None:
    """
    Main async entry point to run all test cases.
    """
    await concurrent()
    await parallel_with_create_tasks()
    await parallel_with_gather()
    await parallel_with_task_groups()


if __name__ == "__main__":
    asyncio.run(main())
