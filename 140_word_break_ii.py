class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.wordBreakHelper(s, wordDict, dict())

    def wordBreakHelper(self, s, wordDict, ansDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if len(s) == 0:
            # print("Empty string found, returning " + str([s]))
            return [s]
        if s in ansDict:
            # print("{0} {1}".format(s, ansDict))
            # print("{0} found in ansDict, returning memoized answer {1}".format(s, ansDict[s]))
            return ansDict[s]
        x = ''
        full_ans = []
        for index, ch in enumerate(s):
            x += ch
            if x in wordDict:
                # print("{0} Found {1} in wordDict, calling wordBreak({2}, {3})".format(s, x, s[index+1:], "wordDict"))
                rem_ans = [rem for rem in self.wordBreakHelper(s[index+1:], wordDict, ansDict)]
                # print("{0} Before {1}".format(s, str(rem_ans)))
                for j, rem in enumerate(rem_ans):
                    if len(rem_ans[j]) != 0:
                        rem_ans[j] = x + " " + rem_ans[j]
                    else:
                        rem_ans[j] = x
                # print("{0} After {1}".format(s, str(rem_ans)))
                full_ans = full_ans + rem_ans
        # print("{0} memoizing answer for {0} as {1}".format(s, full_ans))
        ansDict[s] = full_ans
        # print("{0} {1}".format(s, ansDict))
        # print("{0} returning {1}".format(s, str(full_ans)))
        # print("---------------------------------------------")
        return full_ans