'''
Author: Joseph Tadrous
Description: Test units for csv-combiner.py script
'''

import os
import unittest


class TestCSVCombiner(unittest.TestCase):
    
    def test_real_liverpool(self):
        os.system('python3 csv-combiner.py ./tests/real-madrid.csv ./tests/liverpool.csv > ./tests/test1.csv')
        with open('./tests/real-madrid-liverpool.csv') as ground_truth, open('./tests/test1.csv') as test:
            self.assertEqual(ground_truth.read(), test.read())

    def test_all(self):
        os.system('python3 csv-combiner.py ./tests/real-madrid.csv ./tests/liverpool.csv ./tests/man-city.csv ./tests/man-utd.csv > ./tests/test2.csv')
        with open('./tests/all.csv') as ground_truth, open('./tests/test2.csv') as test:
            self.assertEqual(ground_truth.read(), test.read())

    def test_premier(self):
        os.system('python3 csv-combiner.py ./tests/liverpool.csv ./tests/man-city.csv ./tests/man-utd.csv > ./tests/test3.csv')
        with open('./tests/premier.csv') as ground_truth, open('./tests/test3.csv') as test:
            self.assertEqual(ground_truth.read(), test.read())

    def test_one(self):
        os.system('python3 csv-combiner.py ./tests/real-madrid.csv > ./tests/test4.csv')
        with open('./tests/one.csv') as ground_truth, open('./tests/test4.csv') as test:
            self.assertEqual(ground_truth.read(), test.read())


if __name__ == '__main__':
    unittest.main()