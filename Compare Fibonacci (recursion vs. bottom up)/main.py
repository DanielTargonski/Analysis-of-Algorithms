"""
This project compares the time it takes for different
fibonacci implementations to complete, passed the same number.

Author: Daniel Targonski
"""

import timeit
import pandas as pd
import time

def FiboR(n: int) -> int:
    if n == 1 or n == 0:
        return n
    else:
        return FiboR(n-1) + FiboR(n-2)

def MODFibR(n: int, fibNums: dict) -> int:
    if n < 2:
        fibNums[n] = n
        return fibNums[n]
    elif n in fibNums:
        return fibNums[n]
    else:
        fibNums[n] = MODFibR(n - 1, fibNums) + MODFibR(n - 2, fibNums)
        return fibNums[n]

def FiboNR(n: int) -> int:
    F = []
    F.append(0)
    F.append(1)
    for i in range(2, n+1):
        F.append(F[i-1] + F[i-2])
    return F[n]

MODFibR_Dict = {}
# column names (their list elements will be the column data):
FiboR_list = []
FiboNR_list = []
MODFibR_list = []
fibValues_list = []
int_list = []

# populate the lists will the appropriate information
for i in range(0, 41, 5):
    if i == 0:
        i += 1
    print(i)
    int_list.append(i)

    # Calculate the times for each fib function
    start1 = time.time()
    fib_value = FiboR(i)
    end1 = time.time()
    FiboR_time = end1 - start1

    start2 = time.time()
    fib_value = MODFibR(i, MODFibR_Dict)
    end2 = time.time()
    MODFibR_time = end2 - start2

    start3 = time.time()
    fib_value = FiboNR(i)
    end3 = time.time()
    FiboNR_time = end3 - start3

    fibValues_list.append(fib_value)
    FiboR_list.append(FiboR_time)
    MODFibR_list.append(MODFibR_time)
    FiboNR_list.append(FiboNR_time)

    # fibValues_list.append(MODFibR(i, MODFibR_Dict))
    # FiboR_list.append(timeit.timeit(f"""{FiboR(i)}""", number=10000))
    # MODFibR_list.append(timeit.timeit(f"""{MODFibR(i, MODFibR_Dict)}""", number=10000))
    # FiboNR_list.append(timeit.timeit(f"""{FiboNR(i)}""", number=10000))

numDict = {
    'Integer': int_list,
    "FiboR (seconds)": FiboR_list,
    "MODFibR": MODFibR_list,
    "FiboNR (seconds)": FiboNR_list,
    "Fibo-value": fibValues_list
}



fib_df = pd.DataFrame(numDict)
# If you want the index to be the "Integer" column
# uncomment below:
# fib_df = fib_df.set_index('Integer')
print(fib_df)
