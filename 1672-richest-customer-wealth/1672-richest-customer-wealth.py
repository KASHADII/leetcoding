class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        rows = len(accounts)
        cols = len(accounts[0])
        suma = 0
        
        for i in range(rows):
            for j in range(cols):
                suma = suma + accounts[i][j]
            maxi = max(maxi,suma)
            suma = 0
        return maxi