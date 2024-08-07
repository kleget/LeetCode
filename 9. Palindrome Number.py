class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        y = y[::-1]
        if str(x) == y:
            return True
        else:
            return False

