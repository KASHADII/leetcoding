class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = dict()
        n = len(nums)
        for x in nums:
            dic[x] = dic.get(x,0) + 1
        
        suma = 0

        for i in dic:
            if dic[i] == 1:
                suma = suma + i
        return suma
            
        