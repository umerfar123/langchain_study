import time
import random

import asyncio
from concurrent.futures import ProcessPoolExecutor

"""
When you await a Task, you are subscribing to its completion. If it's already done, you get the result instantly.
If it's still working, you give the Event Loop permission to run other things while you wait.
"""
def fetch_data(size:int):
    
    print('Started Fetching Data Of Size :',size)
    time.sleep(size) # synchronous blocking no switching will happen
    print('Data Fetched Of Size : ',size)
    print()
    return {'data': random.choice(['google','meta','openai','anthropic'])}


async def main():
    
    start = time.perf_counter()
    
    # Since we are creating task in separate threads the blocking synchronous time.sleep() will not pause main event loop
    # so switching to other task is possibl
    
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data,1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data,2 ))

    # since the blocking time.sleep() is in another thread switching is possible to other task
    result1 = await task1
    print("Thread 1 completed")
    result2 = await task2
    print("Thread 2 completed")
    
    
    results = [result1,result2]
    print('Datas Fetched :',results)

    end = time.perf_counter()

    print(f'Time Taken : {end - start:.2f} s')


if __name__ == '__main__':
    asyncio.run(main())