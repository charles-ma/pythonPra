'''
Given an array of nums, return indices of two elements that sum to target. Guaranteed there is one and only one valid pair in the input array
'''

import unittest

# Solution
def twoSum(array, target):
    if array:
        hash = {}
        for i in range(0, len(array)):
            if (target - array[i]) in hash:
                return (hash[target - array[i]], i)
            hash[array[i]] = i                    

# Test cases
class TwoSumTest(unittest.TestCase):
    def test_validCase(self):
        self.assertEqual(twoSum([1, 2, 5, 6], 11), (2, 3))
        self.assertEqual(twoSum([0, -1, 3], 3), (0, 2))
        self.assertEqual(twoSum([-1, 6, -3], 3), (1, 2))
    
    def test_edgeCase(self):
        # Special cases for input array
        self.assertIsNone(twoSum(None, -1))
        self.assertIsNone(twoSum([], 0))
        self.assertIsNone(twoSum([1], 5))

        # No valid tuple in array
        self.assertIsNone(twoSum([-1, -2], 3))
        self.assertIsNone(twoSum([-2, 2, 2, 6, 9], -10))

# Ran tests only when file/module invoked as main
if __name__ == '__main__':
    unittest.main()