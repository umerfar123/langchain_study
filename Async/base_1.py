import asyncio

import time

def sync_func(param :str) -> str:
    print('This is a sync function')
    time.sleep(1)
    
    return f"sync result : {param}"

# async denotes that this function is a asynchronous function / coroutine which the event loop can halt,stop,continue
async def main():
    print("Hello, lets learn aynchio terms")
    
    print(sync_func(param='hello sync'))
    

if __name__ == '__main__':
    # Start the event loop
    # consider event loop as a scheduler that executes task, suspend the task when i/o request comes, and resumes other task
    # we need to run the event loop which will automatically handles everything
    asyncio.run(main())
    