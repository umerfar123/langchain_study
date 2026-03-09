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
    
    # When we call the coroutine fetch_data() it will just return the coroutine object, the coroutine will not be
    # scheduled in the event loop.
    
    task1 = fetch_data(2)
    task2 = fetch_data(4)
    
    # When we await coroutine obj , the main() coroutine will be suspended/paused and fetch_data() coroutine will be 
    # getting scheduled to event loop and will be run untill completion because in event loop there is no 
    # scheduled tasks. Actually we are not getting any concurrency here
    
    result1 = await task1
    result2 = await task2
    
    
    
    results = [result1,result2]
    print('Datas Fetched :',results)

    end = time.perf_counter()

    print(f'Time Taken : {end - start:.2f} s')


if __name__ == '__main__':
    asyncio.run(main())

