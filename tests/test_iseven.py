import unittest

from utilless.iseven import iseven


class TestIsEven(unittest.TestCase):
    def test_iseven(self):
        self.assertTrue(iseven(0))
        self.assertTrue(iseven(2))
        self.assertTrue(iseven(1333533 * 2))
        self.assertTrue(iseven(-42))
        self.assertFalse(iseven(-5))
        self.assertFalse(iseven(1))
        self.assertFalse(iseven(13546843213213654654613))
        with self.assertRaises(TypeError):
            iseven(-5.5)


if __name__ == "__main__":
    unittest.main()
