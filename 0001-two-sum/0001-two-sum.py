class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        rem = 0

        for i in range(n):
            rem = target - nums[i]
            for j in range(n):
                if rem == nums[j] and i != j:
                    return [i,j]
        