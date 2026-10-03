import random

def add_num(a,b):
    sum_result = a+b
    return sum_result

def main():
    while True:
        a,b = random.randint(1,10), random.randint(1,10)
        print(add_num(a,b))
        

if __name__ == '__main__':
    main()