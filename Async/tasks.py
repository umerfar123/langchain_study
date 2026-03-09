import asyncio
import time

async def fetch_stock_price():
    
    print('Started stock price fetching')

    # This pauses fetch_data, allowing the event loop to run other things
    await asyncio.sleep(5)
    
    print("Data received!")
    
    return {"google": 123}

async def fetch_weather():
    
    print("Started Fetching Weather")
    
    await asyncio.sleep(2)
    
    print("Data received!")
    
    return {"mumbai": 30}

async def main():    
    start = time.perf_counter()
    
    task1 = asyncio.create_task(fetch_stock_price())
    task2 = asyncio.create_task(fetch_weather())
    print('task 1 : ',task1)
    print('task2 :',task2)
    
    result1 = await task1
    result2 = await task2
    
    print('Stock Price :',result1)
    print('Weather :',result2)

    end = time.perf_counter()
    
    print(f'Completed In : {end-start:.2f} s')
    
if __name__ == '__main__':
    asyncio.run(main())
    
 
    
    
    
    