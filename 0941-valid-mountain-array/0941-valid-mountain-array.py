class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        maxi = arr[0]
        index = 0

        if n < 3:
            return False

        for i in range(n):
            if arr[i] >= maxi:
                maxi = arr[i]
                index = i
        
        if index == 0 or index == n-1:
            return False

        for i in range(index):
            if arr[i] > arr[i + 1] or arr[i] == arr[i+1]:
                 return False

        for i in range(index+1 , n-1):
            if arr[i] < arr[i+1] or arr[i] == arr[i+1]:
                return False
        
        
        
        
        return True
        


        