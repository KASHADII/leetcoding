class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_count = 0
        temp = []
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])
            if nums[i] == 0:
                zero_count += 1
        for i in range(n - zero_count):
            nums[i] = temp[i]
        for i in range(n - zero_count , n):
            nums[i] = 0
        
