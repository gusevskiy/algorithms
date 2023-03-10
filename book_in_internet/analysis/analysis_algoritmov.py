from typing import Dict, Callable
from datetime import datetime
import time
import functools


execution_time: Dict[str, float] = {}


def time_it(func):
    """calculation of the function operation time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start, func.__name__)
        return result
    return wrapper


def sumOfN(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    end = time.time()
    return theSum, end - start


def foo(tom):
    fred = 0
    for bill in range(1,tom+1):
       barney = bill
       fred = fred + barney

    return fred


def sumOfN3(n):
    start = time.time()
    a =(n*(n+1))/2
    end = time.time()
    return a, end - start


if __name__ == '__main__':
    # print(sumOfN(10000))
    # print(foo(23))
    # print(sumOfN3(23))

    # for i in range(5):
    #     print("Sum is %d required %10.7f seconds" % sumOfN(1000000))
    '''
    Sum is 500000500000 required  0.1192741 seconds
    Sum is 500000500000 required  0.1052041 seconds
    Sum is 500000500000 required  0.1085026 seconds
    Sum is 500000500000 required  0.0883834 seconds
    Sum is 500000500000 required  0.0645332 seconds
    '''
    a = 10000
    for i in range(5):

        print("Sum is %d required %10.7f seconds"%sumOfN3(a))
        a *= 100
    '''
    Sum is 500000500000 required  0.0000026 seconds
    Sum is 500000500000 required  0.0000012 seconds
    Sum is 500000500000 required  0.0000007 seconds
    Sum is 500000500000 required  0.0000005 seconds
    Sum is 500000500000 required  0.0000010 seconds
    '''