
import unittest

from scratch import main

class MyTest(unittest.TestCase):
    
    def test0(self):
        self.assertEqual(main(1), 1)
    
if __name__ == '__main__':
    unittest.main()
    