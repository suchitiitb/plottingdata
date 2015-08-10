import time
import pandas as pd

import cProfile
# import numpy as np
# from datetime import datetime as d
# import sys
# from plot_parameters import *
# import matplotlib
# import matplotlib.pyplot as plt

a = [3,4,5]
b = a[0]


def add_values(a,b):
    s = 1
    d = 3
    k = 4
    e =s*k*d
    return a + b


c = add_values(5,6)

print c
