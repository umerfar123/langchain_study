import time
import random

import asyncio

"""
When you await a Task, you are subscribing to its completion. If it's already done, you get the result instantly.
If it's still working, you give the Event Loop permission to run other things while you wait.
"""
async def fetch_data(size:int):
    
    print('Started Fetching Data Of Size :',size)
    await asyncio.sleep(size)
    print('Data Fetched Of Size : ',size)
    print()
    return {'data': random.choice(['google','meta','openai','anthropic'])}


async def main():
    
    start = time.perf_counter()
    
    # when we create task with coroutine object the coroutine will be scheduled in event loop, so if one task get paused
    # another task can start or resume
    
    task2 = asyncio.create_task(fetch_data(2))
    task1 = asyncio.create_task(fetch_data(1))
    
    """When your code hits result2 = await task2:

    Yielding Control: The main() function says to the Event Loop: "I cannot go any further until task2 is finished. 
    I am pausing myself. Please go deal with the tasks in your queue."

    The Loop Takes Over: The Event Loop looks at its queue. It sees task2 (which needs 2 seconds) and task1 
    (which needs 1 second).

    Execution Starts: It starts task2. task2 hits await asyncio.sleep(2). Now task2 is also paused.

    The Loop Switches: Since task2 is waiting, the loop immediately checks the next item: task1.

    Concurrent Progress: task1 starts, hits await asyncio.sleep(1), and it pauses too."""

  
    result2 = await task2
    print("Task 2 completed")
    result1 = await task1
    print("Task 1 completed")
    
    # if we switch the order of await it will behave differently
    
    
    results = [result1,result2]
    print('Datas Fetched :',results)

    end = time.perf_counter()

    print(f'Time Taken : {end - start:.2f} s')


if __name__ == '__main__':
    asyncio.run(main())

