class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return ''
        if len(strs) is 1:
            return strs[0]
        
        sh = self.shortest(strs)
        common = strs[sh]

        for index in range(len(strs)):
            if index != sh:
                common = self.cmp(common, strs[index])
        return common

    def shortest(self, strs):
        index, slen = 0, 1024;
        for i in range(len(strs)):
            tlen = len(strs[i])
            if slen > tlen:
                index = i
                slen = tlen
        return index

    def cmp(self, s, l):
        for i in range(len(s)):
            if s[i] != l[i]:
                return s[:i]
        return s

    """
    def longestCommonPrefix(self, strs):
        if not len(strs):
            return ''
        strs = sorted(strs)
        return self.cmp(strs[0], strs[-1])
    """
