class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n = len(nums1)
        m = len(nums2)

        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
        
        s = set()
        for x in ans:
            s.add(x)
        sl = list(s)
        return sl
        