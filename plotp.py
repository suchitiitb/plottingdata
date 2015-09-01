import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.style.use('ggplot')
# import line_profiler
# from memory_profiler import profile

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

#@profile
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
    
#     d = {'one' : np.random.rand(10),'two' : np.random.rand(10)}
# 
#     df = pd.DataFrame(d)
# 
#     df.plot(style=['o','rx'])
    
    
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    print ts



if __name__ == "__main__":
    main()

# 
# c = add_values(5,6)
# 
# print c

