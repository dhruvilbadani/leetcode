class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = ""
        i = 0
        min_len = min([len(s) for s in strs])
        while i < min_len:
            i_th_chars = set([s[i] for s in strs])
            if len(i_th_chars) > 1:
                break
            prefix += s[i]
            i += 1
        return prefix