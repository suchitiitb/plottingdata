import os
from os.path import sys
import random
import unittest
# import pandas as pd

#from plotp import add_values
def add_values(a,b):
    return a + b
 
class Testplotp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.a = 1
        cls.b = 2
        
    def test_add_values(self):
        self.assertEqual(add_values(self.a,self.b),3)
        
#comment
      

  
