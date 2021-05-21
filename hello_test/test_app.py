import unittest

from app import Calculator


class TestHaminjuri(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"in setup class-{cls}")

    @classmethod
    def tearDownClass(cls):
        print(f"in tearDown class-{cls}")

    def setUp(self):
        print(f"in setUp-{self}")
        self.calc = Calculator()

    def tearDown(self):
        print(f"in tearDown-{self}")

    def test_true(self):
        self.assertTrue(True)


class CalculatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("in setup class")

    @classmethod
    def tearDownClass(cls):
        print("in tearDown class")

    def setUp(self):
        print("in setUp")
        self.calc = Calculator()

    def tearDown(self):
        print("in tearDown")

    def test_jam(self):
        a, b = 2, 5
        result = self.calc.jam(a, b)
        self.assertEqual(result, 7)

    def test_minus(self):
        a, b = 2, 5
        result = self.calc.minus(a, b)
        self.assertEqual(result, -3)


if __name__ == "__main__":
    unittest.main()
