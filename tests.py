import unittest
from check_pwd import check_pwd


class TestFunc(unittest.TestCase):
    def test1(self):
        self.assertEqual(check_pwd("aA1!aA1!"), True)

    def test2(self):
        self.assertEqual(check_pwd("aA1!aA1"), False)

    def test3(self):
        self.assertEqual(check_pwd("aA1!aA"), False)


if __name__ == '__main__':
    unittest.main()
