import time
import random

import asyncio
from concurrent.futures import ProcessPoolExecutor

"""
In standard Python, you have a Global Interpreter Lock (GIL). This is like having only one "brain" allowed to 
work at a time. Even if your computer has 8 CPU cores, the GIL usually forces Python to use only one for calculations.

Process Pool Executor is the "break glass in case of emergency" tool that bypasses this limit.

How It Works (The "Separate Office" Analogy)
The Manager (Main Process): Your main Python script is the manager. It has the Event Loop running.

The Workers (Child Processes): When you use ProcessPoolExecutor, Python spawns entirely new copies of the Python 
interpreter.

The Hand-off: Because these workers live in "separate offices," they don't share memory. The Manager has to 
"package" (serialize/pickle) the data and the function, send it over to the worker's office, wait for them to finish,
and "unpackage" the result they send back.

Why use it instead of Threads?
Threads (The "Shared Desk" approach): Great for waiting (like time.sleep or downloading a file). However, 
because they share the same "brain" (the GIL), if one thread starts doing heavy math, it blocks all other threads.

Processes (The "Separate Building" approach): Since each process has its own "brain" (its own GIL), 
they can all do heavy math at the exact same time on different CPU cores.
"""
def fetch_data(size:int):
    
    print('Started Fetching Data Of Size :',size)
    time.sleep(size) # synchronous blocking no switching will happen
    print('Data Fetched Of Size : ',size)
    print()
    return {'data': random.choice(['google','meta','openai','anthropic'])}


async def main():
    
    start = time.perf_counter()
    
    # Run in Process Pool
    loop = asyncio.get_running_loop()
    
    # It will move the fetch_data out of main event loop to another process and return the coroutine obj for tracking
    with ProcessPoolExecutor() as executor:
        task1 = loop.run_in_executor(executor, fetch_data, 1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)
        
        # since the blocking time.sleep() is in another process switching is possible to other task
        result1 = await task1
        print("Process 1 completed")
        result2 = await task2
        print("Process 2 completed")
    
    results = [result1,result2]
    print('Datas Fetched :',results)

    end = time.perf_counter()

    print(f'Time Taken : {end - start:.2f} s')


if __name__ == '__main__':
    asyncio.run(main())