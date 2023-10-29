from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c =  Counter(nums).most_common(k)[:k]
        return [x[0] for x in c]

        
