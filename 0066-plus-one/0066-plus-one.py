class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums  = []
        nums = digits
        n = len(nums)
        number = 0

        for i in range(n):
            nums[i] = nums[i] * (10 ** (n - i -1))
            number = number + nums[i]
        number += 1  
        dig = []
        while(number > 0):
            dig.append(number % 10)
            number = number // 10
        
        m = len(dig)
        for i in range(m//2):
            temp = dig[m-i-1]
            dig[m-i-1] = dig[i]
            dig[i] = temp
        return dig



        