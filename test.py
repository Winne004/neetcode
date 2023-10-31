import unittest

from src.containsDuplicates import Solution
from src.isAnagram import Solution as IsAnagramSolution
from src.groupAnagrams import Solution as GroupedAnagramSolution
from src.topKFrequent import Solution as GroupedTopKFrequentSolution
from src.isPalindrome import Solution as IsPalindromeSolution


class Test(unittest.TestCase):
    def test_contains_duplicates(self):
        for nums, expected_result in [([1, 2, 3, 1], True), ([1, 2, 3, 4], False)]:
            result = Solution.containsDuplicate(self, nums=nums)
            self.assertEqual(result, expected_result)

    def test_is_anagram(self):
        for s, t, expected_result in [("anagram", "nagaram", True)]:
            result = IsAnagramSolution.isAnagram(self, s=s, t=t)
            self.assertEqual(result, expected_result)

    def test_group_anagrams(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_result = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        results = GroupedAnagramSolution.groupAnagrams(self, strs=strs)
        for result in results:
            result.sort()
            self.assertIn(result, expected_result)

    def test_topKFrequent(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        result = GroupedTopKFrequentSolution.topKFrequent(self, nums=nums, k=2)
        self.assertEqual(result, [1, 2])

    def test_valid_palindrome(self):
        s = "A man, a plan, a canal: Panama"
        expected_result = True
        result = IsPalindromeSolution.isPalindrome(self, s=s)
        self.assertEqual(result,expected_result)

if __name__ == "__main__":
    unittest.main()
