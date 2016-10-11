class Solution(object):

    _nspaces = {}

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        index, lines = 0, []
        buffer, wordLength, space = [], 0, -1
        while index < len(words):
            word, line = words[index], ''
            if (wordLength + len(word) < maxWidth - space):
                buffer.append(word)
                wordLength += len(word)
                space += 1
                if index == len(words) - 1 and buffer:
                    line = ' '.join(buffer)
                    line += self.nspaces(maxWidth - wordLength - space)
                    lines.append(line)
                index += 1
            else:
                line = self.lineJustify(buffer, maxWidth - wordLength, space)
                lines.append(line)
                buffer, wordLength, space = [], 0, -1

        return lines

    def lineJustify(self, words, total, n):
        if n == 0:
            return words[0] + self.nspaces(total)
        for i in range(total % n):
            words[i] += ' '
        return (self.nspaces(total // n)).join(words)

    def nspaces(self, n):
        if not self._nspaces.get(n):
            self._nspaces[n] = ''.join([' ']* n)
        return self._nspaces[n]
