class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        i, l1, l2 = 0, len(haystack), len(needle)
        if l2 is 0:
            return 0
        for i in range(l1-l2+1):
            if haystack[i] is needle[0] \
            and haystack[i+l2-1] is needle[-1]:
                if haystack[i:i+l2] == needle:
                    return i
        return -1
    #def strStr(self, haystack, needle):
    #    return haystack.find(needle)
