#!/usr/bin/python
import unittest
import main

sample_lines = [
    ('5', 5),
    ('1 3 6 ', -1),
    ('20 !', -1),
    ('12 35', 47),
    ('12   497', -1),
    ('    ', -1),
    ('1000 A', -1),
    ('100 1', 2),
    ('200 3 4', -1),
    ('4 0 19', -1),
    ('9 2', 11),
    ('18 9', 9),
    ('4 -2', -1)]
    

class TestingStringMethods(unittest.TestCase):
    def test_reverse(self):
        """This function tests main method reverse """
        number = '783'
        self.assertEqual(main.reverse(number), '387')

    def test_convertToString(self):
        """This function tests main method convertToString """
        self.assertEqual(main.convertToString(783), '783')

    def test_lineResult(self):
        """This function tests the expected result from a given line"""
        for lineInput, expectResult in sample_lines:
            with self.subTest():
                sumResult = main.reserseSum(lineInput)
                self.assertEqual(sumResult, expectResult)


# running the tests
if __name__ == "__main__":
    unittest.main()
