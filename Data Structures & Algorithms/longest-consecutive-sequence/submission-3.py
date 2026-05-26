class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        max = 0
        for i in set1:
            if i-1 in set1:
                continue
            else:
                count = 1
                j = i
                while j+1 in set1:
                    count = count+1
                    j = j+1
                if count>max:
                    max = count
        
        return max
        