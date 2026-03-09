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

async def retrieve_data(size:int):
    
    print('Started Fetching Data Of Size :',size)
    time.sleep(size) # synchronous blocking no switching will happen
    print('Data Fetched Of Size : ',size)
    print()
    return {'data': random.choice(['ai','ml','dl','agents'])}

async def main():
    
    start = time.perf_counter()
    
    task2 = asyncio.create_task(retrieve_data(2))
    task1 = asyncio.create_task(fetch_data(1))

  
    result2 = await task2
    print("Task 2 completed")
    result1 = await task1
    print("Task 1 completed")
    
    
    results = [result1,result2]
    print('Datas Fetched :',results)

    end = time.perf_counter()

    print(f'Time Taken : {end - start:.2f} s')


if __name__ == '__main__':
    asyncio.run(main())

