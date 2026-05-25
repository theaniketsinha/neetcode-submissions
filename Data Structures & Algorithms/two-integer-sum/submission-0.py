class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # A blank dict
        hashmap = {}

        # Creating hashmap
        for i in range(len(nums)):
            hashmap[i]=nums[i]

        #Checking the element in hashmap
        for i in range(len(nums)):
            complement = target - nums[i]
            for j in hashmap:
                if hashmap[j] == complement and i != j:
                    return sorted([i, j])
        
        return []