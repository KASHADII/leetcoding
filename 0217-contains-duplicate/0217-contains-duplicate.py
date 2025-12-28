class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seti = set()
        
        for i in range(n):
            seti.add(nums[i])
        len_set = len(seti)

        if n == len_set:
            return False
        else:
            return True
