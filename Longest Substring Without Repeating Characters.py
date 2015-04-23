class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        left=0
        right=1
        longest= s[0] if len(s) else ''
        while right < len(s):
            tmp = s[left:right]
            if s[right] not in tmp:
                right+=1
                tmp = s[left:right]
                if len(tmp)>len(longest):
                    longest = tmp;
            else:
                left+=1
        return len(longest)