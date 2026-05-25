class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)

        l1 = []
        for i in counter.values():
            l1.append(i)
        
        l1.sort(reverse = True)

        l2 = []
        for i in range(k):
            target_freq = l1[i]
            for key, value in counter.items():
                if value == target_freq and key not in l2:
                    l2.append(key)
                    break

        return l2
