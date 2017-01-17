from collections import Counter, defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        count, total = defaultdict(int),Counter(words)
        step, n, result = len(words[0]), len(words), []
        for i in range(len(s)-step*n+1):
            count.clear()
            for j in range(0, step*n, step):
                word = s[i+j: i+j+step]
                if word in total:
                    count[word] += 1
                else:
                    break
            if count == total:
                result.append(i)
        return result
