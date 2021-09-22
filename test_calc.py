import unittest
from calc import Clac

class TestCalc(unittest.TestCase):

    def test_add(self):
        set_1 = Clac(10,5)
        set_2 = Clac(-1,1)
        set_3 = Clac(-1,-1)
        self.assertEqual(set_1.add(), 15)
        self.assertEqual(set_2.add(), 0)
        self.assertEqual(set_3.add(), -2)

    def test_subtract(self):
        set_1 = Clac(10, 5)
        set_2 = Clac(-1, 1)
        set_3 = Clac(-1, -1)
        self.assertEqual(set_1.subtract(), 5)
        self.assertEqual(set_2.subtract(), -2)
        self.assertEqual(set_3.subtract(), 0)

    def test_multiply(self):
        set_1 = Clac(10, 5)
        set_2 = Clac(-1, 1)
        set_3 = Clac(-1, -1)
        self.assertEqual(set_1.multiply(), 50)
        self.assertEqual(set_2.multiply(), -1)
        self.assertEqual(set_3.multiply(), 1)

    def test_divide(self):
        set_1 = Clac(10, 5)
        set_2 = Clac(-1, 1)
        set_3 = Clac(-1, -1)
        set_4 = Clac(5,2)
        set_5 = Clac(10,0)
        self.assertEqual(set_1.divide(), 2)
        self.assertEqual(set_2.divide(), -1)
        self.assertEqual(set_3.divide(), 1)
        self.assertEqual(set_4.divide(), 2.5)

        with self.assertRaises(ValueError):
            set_5.divide()


if __name__ == '__main__':
    unittest.main()