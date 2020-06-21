import unittest

from utilless.isodd import isodd


class TestIsOdd(unittest.TestCase):
    def test_isodd(self):
        self.assertFalse(isodd(0))
        self.assertFalse(isodd(2))
        self.assertFalse(isodd(1333533 * 2))
        self.assertFalse(isodd(-42))
        self.assertTrue(isodd(-5))
        self.assertTrue(isodd(1))
        self.assertTrue(isodd(13546843213213654654613))
        with self.assertRaises(TypeError):
            isodd(-5.5)


if __name__ == "__main__":
    unittest.main()
