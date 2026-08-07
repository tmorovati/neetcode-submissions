class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        output = []
        for str in strs: 
            key = tuple(sorted(str))
            hashmap[key].append(str)
        
        return list(hashmap.values())