import time
import random

import asyncio

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
    
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    
    # When we await task1, since its already is scheduled in the event loop, directly the execution will start ,
    # if it gets paused, the task2 will can get started / resumed. 

    # awaiting task2 first doesn't mean it will get executed first, its depends on the order which the task are scheduled
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

