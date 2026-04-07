class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        i str s
        o T/F if palindrome(same forward and backward)
        c case-insensitive, ignore non-alph only a-z|0-9
        e empty
        """
        cleanS = ''.join(char.lower() for char in s if char.isalnum())

        return cleanS == cleanS[::-1]