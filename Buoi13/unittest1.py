import unittest

def add(a,b):
    return a + b

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2,3), 5)


if __name__ == "__main__":
    unittest.main()