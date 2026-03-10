import unittest
from extreme_programming.exercise2.ex2 import convertToInt


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(convertToInt("X"), 10)

    def test2(self):
        self.assertEqual(convertToInt("I"), 1)

    def test3(self):
        self.assertEqual(convertToInt("VI"), 6)

    def test4(self):
        self.assertEqual(convertToInt("m"), -9999)

    def test5(self):
        self.assertEqual(convertToInt("IL"), -9999)

    def test6(self):
        self.assertEqual(convertToInt("LL"), -9999)

    def test7(self):
        self.assertEqual(convertToInt("MMMCMXCIX"), 3999)

    def test8(self):
        self.assertEqual(convertToInt(10), -9999)

    def test9(self):
        self.assertEqual(convertToInt("IXIX"), -9999)

    def test10(self):
        self.assertEqual(convertToInt("IXX"), -9999)

    def test11(self):
        self.assertEqual(convertToInt("VIV"), -9999)

    def test12(self):
        self.assertEqual(convertToInt("XVI"), 16)

    def test13(self):
        self.assertEqual(convertToInt("CDC"), -9999)

    def test14(self):
        self.assertEqual(convertToInt("IC"), -9999)

    def test15(self):
        self.assertEqual(convertToInt("IIV"), -9999)

    def test16(self):
        self.assertEqual(convertToInt("XCX"), -9999)


test = Tests()
