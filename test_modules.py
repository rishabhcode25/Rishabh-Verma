import unittest

class TestModules(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_another_example(self):
        self.assertTrue(isinstance('hello', str))

if __name__ == '__main__':
    unittest.main()