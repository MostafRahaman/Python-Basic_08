import Code_Coverage.My_math as My_math
import unittest
class TestAdd(unittest.TestCase):
    def test_add_integer(self):
        result = My_math.add(10, 5)
        self.assertEqual(result, 25)
if __name__ == '__main__':
    unittest.main()