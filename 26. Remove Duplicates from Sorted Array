class Solution:
    def removeDuplicates(self, nums: List[int]):
        i = 0
        k = 1

        while i <= len(nums)+1:
            try:
                if nums[i+1] != '_':
                    if nums[i] == nums[i + 1]:
                        del nums[i + 1]
                        nums.append('_')
                    else:

                        k += 1
                        i += 1
                else:
                    return k
            except:
                return k
