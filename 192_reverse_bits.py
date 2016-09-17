class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        reverse = 0
        power = 31
        while n > 0:
            bit = n%2
            reverse += (bit * (2 ** power))
            power -= 1
            n = n//2
        return reverse

sol = Solution()
print(sol.reverseBits(100))