class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = dict()
        n = len(nums)
        ans = []

        for x in nums:
            d[x] = d.get(x,0) + 1

        for i in range(1,n+1):
            if i not in d:
                ans.append(i)
        return ans

        

        