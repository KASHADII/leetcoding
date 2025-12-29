class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = abs(nums[i])
        nums.sort()
        for i in range(n):
            nums[i] = nums[i] ** 2
        return nums
        