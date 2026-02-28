import unittest
from extreme_programming.exercise1.ex1 import wrap

class WrapTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(wrap("ahoj", 10), "ahoj")

    def test_2(self):
        self.assertEqual(wrap("abcd", 4), "abcd")

    def test_3(self):
        self.assertEqual(wrap("Four score", 7), "Four\nscore")

    def test_4(self):
        self.assertEqual(wrap("ab cd", 5), "ab cd")

    def test_5(self):
        self.assertEqual(wrap("Fifteen", 4), "Fift\neen")

    def test_6(self):
        self.assertEqual(wrap("hi abcdef", 4), "hi\nabcd\nef")

    def test_7(self):
        self.assertEqual(wrap("Ahoj\nsvet", 10), "Ahoj\nsvet")

    def test_8(self):
        self.assertEqual(wrap("Ahoj\n\nsvet", 10), "Ahoj\n\nsvet")

    def test_9(self):
        self.assertEqual(wrap("Ahoj\n     \nsvet", 10), "Ahoj\n\nsvet")

    def test_10(self):
        self.assertEqual(wrap("Ahoj\n     \nsvet", 0), "")

    def test_11(self):
        self.assertEqual(wrap("abcdefghijKL mn", 5), "abcde\nfghij\nKL mn")

    def test_12(self):
        self.assertEqual(wrap("aaaa bbbb ccccccc dddddddddd eee fffffffffffffffffffffffffffffffffff ggg", 10), "aaaa bbbb\nccccccc\ndddddddddd\neee\nffffffffff\nffffffffff\nffffffffff\nfffff ggg")

if __name__ == "__main__":
    unittest.main()