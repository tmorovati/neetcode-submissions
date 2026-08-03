class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optimum Solution using O(n)
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        # using bucket sort 
        bucket = [[] for _ in range(len(nums)+1)]
        for element, freq in hashmap.items():
            bucket[freq].append(element)
        
        res = []
        for i in range(len(nums), 0 , -1):
            for element in bucket[i]:
                res.append(element)
            if len(res) == k: 
                return res


