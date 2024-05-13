import unittest
from check_pwd import check_pwd


class TestFunc(unittest.TestCase):
    def test1(self):
        self.assertEqual(check_pwd("12345678"), True)



if __name__ == '__main__':
    unittest.main()
