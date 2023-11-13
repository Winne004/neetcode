class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = [char.lower() for char in s if char.isalnum()]
        tmp = "".join(tmp)
        return tmp == tmp[::-1]

    def isPalindrome2(self, s: str) -> bool:
        cleaned_chars = [char.lower() for char in s if char.isalnum()]

        left, right = 0, len(cleaned_chars) - 1
        while left < right:
            if cleaned_chars[left] != cleaned_chars[right]:
                return False

            left += 1
            right -= 1

        return True
