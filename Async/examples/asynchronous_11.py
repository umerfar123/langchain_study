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
    
    coroutines = [fetch_data(i) for i in range(1,3)]
    results = await asyncio.gather(*coroutines,return_exceptions=True)
    # return exeception = True will run all coroutines even if, any one of them fails and send the results back in 
    # order of coroutines given
    
    print('Datas Fetched :',results)

    end = time.perf_counter()

    print(f'Time Taken : {end - start:.2f} s')


if __name__ == '__main__':
    asyncio.run(main())