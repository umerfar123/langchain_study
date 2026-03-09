import time
import random

import asyncio
from concurrent.futures import ProcessPoolExecutor

def fetch_data(size:int):
    
    print('Started Fetching Data Of Size :',size)
    time.sleep(size) # synchronous blocking no switching will happen
    print('Data Fetched Of Size : ',size)
    print()
    return {'data': random.choice(['google','meta','openai','anthropic'])}


async def main():
    
    start = time.perf_counter()
    
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data,1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data,2 ))

    results = await asyncio.gather(task1, task2)
    
    print('Datas Fetched :',results)

    end = time.perf_counter()

    print(f'Time Taken : {end - start:.2f} s')


if __name__ == '__main__':
    asyncio.run(main())