import unittest
from math import pow
 
class TestUM(unittest.TestCase):
 
    def setup(self):
        pass
 
    def test_first_3_4(self):
        
        self.assertEqual( pow(2,3), 8)
 
    def test_second_a_3(self):
        self.assertEqual( max(1,2,3),3)
 
if __name__ == '__main__':
    unittest.main()
