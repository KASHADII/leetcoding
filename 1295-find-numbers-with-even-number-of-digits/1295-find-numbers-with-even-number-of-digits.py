class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            dig_count =0 
            num = nums[i]
            str_num = str(nums[i])
            for j in range(len(str_num)):
                num = num // 10
                dig_count += 1
            if dig_count % 2 == 0:
                count += 1
        return count
            
            
        