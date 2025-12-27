class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        
        suma = 0
        maxi = 0

        for i in range(n):
            suma = suma + gain[i]
            maxi = max(maxi,suma)
        return maxi

