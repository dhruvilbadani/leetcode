class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == None or len(digits) == 0:
            return []
        digit_to_letters = dict()
        digit_to_letters['2'] = ['a', 'b', 'c']
        digit_to_letters['3'] = ['d', 'e', 'f']
        digit_to_letters['4'] = ['g', 'h', 'i']
        digit_to_letters['5'] = ['j', 'k', 'l']
        digit_to_letters['6'] = ['m', 'n', 'o']
        digit_to_letters['7'] = ['p', 'q', 'r', 's']
        digit_to_letters['8'] = ['t', 'u', 'v']
        digit_to_letters['9'] = ['w', 'x', 'y', 'z']
        first_choices = digit_to_letters[digits[0]]
        rest_of = self.letterCombinations(digits[1:])
        results = set()
        if len(rest_of) == 0:
            return first_choices
        for first_choice in first_choices:
            for rest in rest_of:
                results.add(first_choice + rest)
        return list(results)