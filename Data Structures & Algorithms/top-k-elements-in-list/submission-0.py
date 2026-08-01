class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
    
        # sort (num, count) pairs by count, ascending
        sorted_items = sorted(hashmap.items(), key=lambda pair: pair[1])
        top_k = sorted_items[-k:]          # last k = highest counts
        return [num for num, count in top_k]
        
            
            