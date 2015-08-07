import unittest
# import pandas as pd
import random
import os
from os.path import sys
#sys.path.append('C:\Users\ct000187\git\plottingdata\plotp.py')



#from plotp import add_values
def add_values(a,b):
    return a + b
 
class TestPlotp(unittest.TestCase):    
    @classmethod
    def setUpClass(cls):
        cls.a = 1
        cls.b = 2
        
    def test_add_values(self):
        self.assertEqual(add_values(cls.a,cls.b),3)
        
        
      

  
