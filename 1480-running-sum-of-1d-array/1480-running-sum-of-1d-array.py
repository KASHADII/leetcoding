class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum = nums[0]
        for i in range(1,n):
            sum = sum + nums[i]
            nums[i] = sum
        return nums
        