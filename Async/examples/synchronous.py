import time
import random

def fetch_data(size:int):
    
    print('Started Fetching Data Of Size :',size)
    time.sleep(size)
    print('Data Fetched Of Size : ',size)
    print()
    return {'data': random.choice(['google','meta','openai','anthropic'])}


def main():
    
    result1 = fetch_data(2)
    result2 = fetch_data(4)
    
    return [result1,result2]


start = time.perf_counter()

results = main()

print('Data Fetched :',results)

end = time.perf_counter()

print(f'Time Taken : {end - start:.2f} s')