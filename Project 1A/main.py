"""
This project is to demonstrate the proper 
fib numbersfrom a ModFib algorithm.

Author: Daniel Targonski
"""
import pandas as pd
import time

def ModRecursive(num: int, fibDict: dict) -> int:
    '''
    Args:
    num (int): Fibonacci number to calculate
    fibDict (dict): Stores completed fibonacci calculations

    Returns (int): fibonacci value
    '''
    if num < 2:
        fibDict[num] = num
        return fibDict[num]
    elif num in fibDict:
        return fibDict[num]
    else:
        fibDict[num] = ModRecursive(num - 1, fibDict) + ModRecursive(num - 2, fibDict)
        return fibDict[num]

fib_nums = {}
fib_results = []
num_list = []
modFib_time_list = []

for i in range(0, 101, 5):
    if i == 0:
        i = 1

    num_list.append(i)

    time_start = time.time()

    fib_results.append(ModRecursive(i, fib_nums))

    time_end = time.time()

    ModFib_time_result = time_end - time_start
    modFib_time_list.append(ModFib_time_result)

results_dict = {
    "n": num_list,
    "ModRecursive (seconds)": modFib_time_list,
    "Fibonacci": fib_results
}

fib_pd = pd.DataFrame(results_dict)
print(fib_pd)