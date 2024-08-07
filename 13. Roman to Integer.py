class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        s = list(s)
        for x in range(len(s)):
            s[x] = alphabet[s[x]]
        for y in range(len(s) - 1):
            if s[y] < s[y + 1]:
                s[y + 1] = s[y + 1] - s[y]
                s[y] = 0

        return sum(s)
