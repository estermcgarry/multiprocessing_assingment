import time
import math
import multiprocessing
from multiprocessing import Pool


def check_prime(num):
    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:", int(time.time()-t1))
                break
        else:
            print(num,"is a prime number")
            print("Time:", time.time()-t1)
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    return res

def check_prime_multi(my_dict):
    num = my_dict["number"]
    lower = my_dict["lower"]
    upper = my_dict["upper"]


    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(lower, upper):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:", int(time.time()-t1))
                break
        else:
            print(num,"prime number not confirmed")
            print("Time:", time.time()-t1)
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    print("Task", multiprocessing.current_process(), num, res)
    return res

