class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        nums.sort()

        result=set()
        if l<3:
            return result
        for a in range(l-2):
            b = a+1
            c = l-1

            while b < c:
                if nums[a]+nums[b]+nums[c]==0:
                    result.add((nums[a], nums[b], nums[c]))
                    b = b+1
                    c = c-1
                elif nums[a]+nums[b]+nums[c]>0:
                    c = c-1
                elif nums[a]+nums[b]+nums[c]<0:
                    b = b+1
            
        return [list(x) for x in result]

