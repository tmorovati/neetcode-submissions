class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using hashmap:
        if len(s) != len(t):
            return False
        
        hashmap_s, hashmap_t = {},{}
        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i] ,0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i] ,0)


        if hashmap_s.keys() != hashmap_t.keys(): # time and space O? 
            return False
        
        for key, val in hashmap_s.items():
            if hashmap_s[key] != hashmap_t[key]: 
                return False
        return True
