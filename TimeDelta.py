#SOLUTION FOR TIME DELTA

import math
import os
import random
import re
import sys
from datetime import datetime as dt
fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) - 
                   dt.strptime(input(), fmt)).total_seconds())))
                   # Complete the time_delta function below.
stdin = sys.stdin
def time_delta(t1, t2):

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        t = int(input())

        for t_itr in range(t):
            t1 = input()

            t2 = input()

            delta = time_delta(t1, t2)

            fptr.write(delta + '\n')

        fptr.close()
        
