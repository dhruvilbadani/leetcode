class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        hammings = [0 for _ in range(num+1)]
        hammings[1] = 1
        for i in range(2, num+1):
            hammings[i] = (i%2) + hammings[i//2]
        return hammings

sol = Solution()
print(sol.countBits(20))