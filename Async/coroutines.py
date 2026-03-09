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
    
    result1 = await fetch_stock_price()
    print('Stock Price :',result1)
    result2 = await fetch_weather()
    print('Weather :',result2)
    
    end = time.perf_counter()
    
    print(f'Completed In : {end-start:.2f} s')
    
if __name__ == '__main__':
    asyncio.run(main())
    
 
    
    
    
    