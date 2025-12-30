class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]
        index = 0

        for i in range(1 , n):
            if nums[i] > maxi:
                maxi = nums[i]
                index = i
        
        for i in range(n):
            if maxi < (nums[i] * 2) and i != index:
                return -1
        return index
        