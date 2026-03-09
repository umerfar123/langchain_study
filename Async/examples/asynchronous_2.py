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
    
    # Here we are creating task for coroutine fetch_data() which will schedule fetch_data() in event loop so that
    # if any other task gets paused we can resume this task
    task1 = asyncio.create_task(fetch_data(2))
    # since we are directly awaiting the task without scheduling another task there is no concurrency here
    result1 = await task1
    
    task2 = asyncio.create_task(fetch_data(4))
    result2 = await task2
    
    # When we await task1, since its already is scheduled in the event loop, directly the execution will start ,
    # if it gets paused, the task2 will can get started / resumed. 

    
    results = [result1,result2]
    print('Datas Fetched :',results)

    end = time.perf_counter()

    print(f'Time Taken : {end - start:.2f} s')


if __name__ == '__main__':
    asyncio.run(main())

