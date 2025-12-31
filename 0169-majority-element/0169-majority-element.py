class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        n = len(nums)
        
        for x in nums:
            dic[x] = dic.get(x,0) + 1

        for x in dic:
            if dic[x] > n/2:
                return x
        