class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        stringed = str(x)
        length = len(stringed)
        for i, char in enumerate(stringed[0:length//2]):
            if char != stringed[length - 1 - i]:
                return False

        return True
