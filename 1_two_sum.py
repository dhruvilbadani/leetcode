class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = dict()
        indices_map = dict()
        for index, num in enumerate(nums):
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1
            if num in indices_map:
                indices_map[num].add(index)
            else:
                indices_map[num] = set([index])
        for index, num in enumerate(nums):
            nums_map[num] -= 1
            if nums_map[num] == 0:
                nums_map.pop(num)
            indices_map[num].remove(index)
            new_target = target - num
            if new_target in nums_map:
                return [index, next(iter(indices_map[new_target]))]
            if num in indices_map:
                indices_map[num].add(index)
            else:
                indices_map[num] = set([index])
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1  
        return None

sol = Solution()
print(sol.twoSum([2, 2, 2, 7], 4))