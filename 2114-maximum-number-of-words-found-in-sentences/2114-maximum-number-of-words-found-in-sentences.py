class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n = len(sentences)
        
        maxi = 0

        for i in range(n):
            s = sentences[i]
            count = 0
            for char in s:
                if char == " ":
                    count += 1
            maxi = max(maxi , count)

            
        return maxi + 1
        