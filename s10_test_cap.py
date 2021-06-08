import unittest

import s9_cap


# we inherit unittest.TestCase class
class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = s9_cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_word(self):
        text = 'monty python'
        result = s9_cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()
