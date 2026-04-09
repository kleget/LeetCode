from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] == 10:
            k = len(digits) -1
            while k > 0:
                if digits[k] == 10:
                    digits[k-1] += 1
                    digits[k]=0
                k-=1
        if digits[0] == 10:
            del(digits[0])
            digits.append(1)
            digits.append(0)
            digits = digits[-2:]+digits[:-2]

        return digits

obj = Solution()
print (obj.plusOne([9, 9]))