import time
import pandas as pd

import line_profiler
from memory_profiler import profile

# import kernprof
# from profile import Profile
# import profile
# import numpy as np
# from datetime import datetime as d
# import sys
# from plot_parameters import *
# import matplotlib
# import matplotlib.pyplot as plt

a = [3,4,5]
b = a[0]

@profile
def add_values(a,b):
    s = 1
    d = 3
    k = 4
    e =s*k*d
    return a + b



def main():
    
    a = 1
    b = 2
    c = add_values(a, b)
    print c

if __name__ == "__main__":
    main()

# 
# c = add_values(5,6)
# 
# print c

