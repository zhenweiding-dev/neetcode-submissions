class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        i str s
        o T/F if palindrome(same forward and backward)
        c case-insensitive, ignore non-alph only a-z|0-9
        e empty
        """
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True