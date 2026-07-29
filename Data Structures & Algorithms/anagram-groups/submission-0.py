class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def isAnagram(word1:str, word2: str) -> bool:
            if len(word1) != len(word2): 
                return False

            word1_sorted = sorted(word1)
            word2_sorted = sorted(word2)
            return word1_sorted == word2_sorted

        
        output = []
        used = [False] * len(strs)

        for idx1 in range(len(strs)): 
            # temp = []
            # temp.append(word)
            if used[idx1]:
                continue

            
            group = [strs[idx1]]
            used[idx1] = True
            for idx2 in range(idx1 + 1 , len(strs)):
                if not used[idx2] and isAnagram(strs[idx1] , strs[idx2]):  
                    group.append(strs[idx2])
                    used[idx2] = True
            output.append(group)
            
            # strs.remove(output[idx1].split()) # remove, append, sort

        return output
         



