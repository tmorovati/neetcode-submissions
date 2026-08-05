class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Forcing
        output = []
        temp = 1
        for i in range(len(nums)):
            for j in range(len(nums)): 
                if j != i: 
                    temp = temp * nums[j]
            output.append(temp)
            temp = 1 
        return output