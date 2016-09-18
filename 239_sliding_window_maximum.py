class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == None:
            return None
        if len(nums) == 0:
            return []
        N = len(nums)
        return [max(nums[i:i+k]) for i in range(N-k+1)]