class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        n = len(nums)
        s = set()

        for i in range(n):
            s.add(nums[i])

        m = len(s)

        for x in s:
            if x > first:
                third = second
                second = first
                first = x

            elif x > second and x < first:
                third = second
                second = x
            elif x > third and x < first and x < second:
                third = x
        
        if m < 3:
            return first
        else:
            return third
        