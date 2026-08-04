class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using time complexity : O(nlogn)
        # space complexity : O(n)
        if len(s) != len(t):
            return False

        # Sorting
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t

        