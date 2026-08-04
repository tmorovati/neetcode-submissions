class Solution:
    # key = '#'
    def encode(self, strs: List[str]) -> str:
        temp = ''
        for string in strs:
            intgr = len(string)
            temp += f'{intgr}#{string}'
        
        return temp 

    def decode(self, s: str) -> List[str]:
        out_str = []
        i = 0 
        while i < len(s): 
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j+1
            end = start + length
            out_str.append(s[start:end])
            i = end 



        return out_str
