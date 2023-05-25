import unittest
import basics


class TestBasic(unittest.TestCase):
    def test_add_profile(self):
        self.assertEqual(basics.add(a=1,b= 2), 3)
        self.assertEqual(basics.add(a= -1,b= 2), 1)
        self.assertEqual(basics.add(a=1,b= -2), -1)
        self.assertEqual(basics.add(a=-1,b= -2), -3)
        pass

    def test_sub_profile(self):
        self.assertEqual(basics.sub(a=1, b= 2), -1)
        self.assertEqual(basics.sub(a=-1,b= 2), -3)
        self.assertEqual(basics.sub(a=-1, b=-2), 1)
        self.assertEqual(basics.sub(a=1, b=-2), 3)
        pass

    def test_multiply_profile(self):
        self.assertEqual(basics.multiply(1, 2), 2)
        self.assertEqual(basics.multiply(-1, 2), -2)
        self.assertEqual(basics.multiply(1, -2), -2)
        self.assertEqual(basics.multiply(-1, -2), 2)
        pass

    def test_divide_profile(self):
        self.assertEqual(basics.divide(15, 5), 3)
        pass