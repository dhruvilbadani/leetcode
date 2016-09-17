class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        return (n%2) + self.hammingWeight(n//2)

sol = Solution()
print(sol.hammingWeight(20))