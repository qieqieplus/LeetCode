class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        tokens = self.tokenizer(p)
        if len(tokens) and tokens[0] != '*':
            l = len(tokens[0])
            if not self.match(s[:l], tokens[0]):
                return False
            s = s[l:]
            tokens.pop(0)
        if len(tokens) and tokens[-1] != '*':
            l = len(tokens[-1])
            if not self.match(s[0-l:], tokens[-1]):
                return False
            s = s[: 0-l]
            tokens.pop(-1)
        if len(s) and not len(tokens):
            return False

        for t in tokens:
            if t != '*':
                left = self.leftSearch(s, t)
                if left < 0:
                    return False
                s = s[left+len(t):]

        return True        

    def tokenizer(self, p):
        ls, token = [], ''
        for ch in p:
            if (ch != '*'):
                token += ch
            else:
                if len(token):
                    ls.append(token)
                    token = ''
                ls.append(ch)
        if len(token):
            ls.append(token)
        return ls

    def match(self, str, token):
        sLen, tLen = len(str), len(token)
        if (sLen != tLen):
            return False
        for i in range(sLen):
            if(token[i] != str[i] and token[i] != '?'):
                return False
        return True

    def leftSearch(self, a, b):
        i, j = 0, 0
        while i+j < len(a):
            if a[i+j] != b[j] and b[j] != '?':
                i, j = i+1, 0
            else:
                j += 1
                if j == len(b):
                    return i
        return -1
