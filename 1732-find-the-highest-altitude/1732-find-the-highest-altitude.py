class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        maxi = 0
        suma = 0
        for i in range(n):
            suma = suma + gain[i]
            maxi = max(suma , maxi)

        return maxi
        