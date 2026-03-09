import time
import random

import asyncio
from concurrent.futures import ProcessPoolExecutor

async def fetch_data(size:int):
    
    print('Started Fetching Data Of Size :',size)
    time.sleep(size) # synchronous blocking no switching will happen
    print('Data Fetched Of Size : ',size)
    print()
    return {'data': random.choice(['google','meta','openai','anthropic'])}


async def main():
    
    start = time.perf_counter()
    
    async with asyncio.TaskGroup() as tg:
        results = [tg.create_task(fetch_data(i)) for i in range(1,3)]
    # Here if any task fails, no other task will be executed, it will return execptions for all tasks
    
    print('Datas Fetched :',[result.result() for result in results])

    end = time.perf_counter()

    print(f'Time Taken : {end - start:.2f} s')


if __name__ == '__main__':
    asyncio.run(main())