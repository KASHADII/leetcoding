class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        

        nums.sort()
        product1 = nums[0] * nums[1] * nums[n-1]
        product2 = nums[n-2] * nums[n-3] * nums[n-1]

        if product1 > product2:
            return product1
        else:
            
            return product2
        


        
             