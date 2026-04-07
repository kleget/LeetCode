from typing import List

class Solution:
        
    def one(self, a):
        if self.target <= a:  self.answer.append(0) #return self.nums.index(a)
        else: self.answer.append(1) #return self.nums.index(a)+1

    def two(self, a, plusminus):
        # if plusminus: self.answer.append(+2)
        if self.target <= a[0]: self.answer.append(0)  # return self.nums.index(a[0])
        elif self.target <= a[1]: self.answer.append(1)# return self.nums.index(a[1])
        else: self.answer.append(2)  #return self.nums.index(a[1])+1

    def more(self, a, plusminus):
        if len(a) == 1:
            self.answer.append(0)
            self.one(a[0])
        elif len(a) == 2:
            # self.answer.append(+2)
            self.two(a, plusminus)
        elif len(a) % 2 == 1: # если нечетные
            if self.target <= a[(len(a)//2)]: # левая граница
                # if plusminus: self.answer.append((len(a)//2)+1) # коретка в начале должна быть
                
                self.more(a[0: (len(a)//2)+1], 0) # граница левая, поэтому не добавляем
            else:
                self.answer.append((len(a)//2)+1)  #if plusminus: self.answer.append((len(a)//2)+1) 
                self.more(a[(len(a)//2)+1: len(a)], 1)
        else: # если четные
            if self.target <= a[(len(a)//2)-1]: # первая
                # if plusminus: self.answer.append((len(a)//2)) # коретка в начале должна быть
                self.more(a[0: (len(a)//2)-1], 0)
            else: 
                self.answer.append((len(a)//2)) 
                self.more(a[len(a)//2: len(a)], 1)

    def searchInsert(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        self.answer = [] 
        if len(self.nums) == 1:
            self.one(self.nums[0])
        elif len(self.nums) == 2:
            # self.answer.append(+2)
            self.two(self.nums, 0)
        elif len(self.nums) >= 3:
            self.more(self.nums, 0)
        return sum(self.answer)


obj = Solution()
res = obj.searchInsert([1,3,4,5,10], 2)
print(res)