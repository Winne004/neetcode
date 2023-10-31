from typing import Deque, List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fast, slow = 0, 0
        seen = set()
        res = 0
        while fast < len(s):
            if s[fast] in seen:
                seen.clear()
                res = max(res, fast-slow)
                slow += 1
                fast = slow
            else:
                seen.add(s[fast])
                fast += 1

        return max(res, fast-slow)


