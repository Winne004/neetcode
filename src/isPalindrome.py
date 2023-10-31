class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = [char.lower() for char in s if char.isalnum()]
        tmp = "".join(tmp)
        return tmp == tmp[::-1]