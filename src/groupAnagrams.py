from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)

        for anagram in strs:
            grouped_anagrams[tuple(sorted(anagram))].append(anagram)

        return grouped_anagrams.values()
