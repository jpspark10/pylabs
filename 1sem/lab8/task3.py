import asyncio


async def conduct_task(name, task_number, preparation_time, defense_time):
    print(f"{name} started the {task_number} task.")
    await asyncio.sleep(preparation_time / 100)
    print(f"{name} moved on to the defense of the {task_number} task.")
    await asyncio.sleep(defense_time / 100)
    print(f"{name} completed the {task_number} task.")


async def handle_candidate(name, prep1, defense1, prep2, defense2):
    await conduct_task(name, 1, prep1, defense1)
    print(f"{name} is resting.")
    await asyncio.sleep(5 / 100)
    await conduct_task(name, 2, prep2, defense2)


async def interviews(*candidates):
    tasks = [handle_candidate(name, prep1, defense1, prep2, defense2) for name, prep1, defense1, prep2, defense2 in
             candidates]
    await asyncio.gather(*tasks)


async def main():
    candidates = [
        ("Alice", 100, 50, 200, 75),
        ("Bob", 80, 60, 150, 90),
        ("Charlie", 120, 70, 180, 100)
    ]
    await interviews(*candidates)


if __name__ == "__main__":
    asyncio.run(main())
