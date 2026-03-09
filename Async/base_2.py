import asyncio


# Only in async functions: You cannot use await in a regular def function. It will throw a SyntaxError.

# It must be "Awaitable": You can only await objects like Coroutines (functions defined with async def), 
# Tasks, or Futures.

# Non-blocking: While await pauses the current function, the Event Loop (the engine running everything) stays 
# active to handle other pending tasks.

# await - Stop here, pause this specific function, and go do other work until this task is finished.


# Coroutine: special type of functions that can be paused, resumed
async def fetch_data():
    print('Starting request')
    
    # This pauses fetch_data, allowing the event loop to run other things
    await asyncio.sleep(2)
    
    print("Data received!")
    return {"data": 123}


async def main():
    
    coroutine_obj = fetch_data()
    print('Coroutine Obj :',coroutine_obj)
     # When you call a async funtion it won't run the code inside, it returns a coroutine object which can awaited.
    result = await coroutine_obj
    # with await if io operation comes in fetch data then event loop will pause the execution and starts and resumes other tasks.
    print(result)
    

if __name__ == '__main__':
    asyncio.run(main())
    