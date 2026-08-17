class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxfar=nums[0]
        currentmax=nums[0]

        for num in nums[1:]:
            currentmax=max(num,currentmax + num)
            maxfar=max(maxfar , currentmax)

        return maxfar