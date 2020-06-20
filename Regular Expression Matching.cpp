class Solution {
public:
	bool isMatch(const string& s, const string& p, int i = 0, int j = 0) {
		auto sLen = s.size(), pLen = p.size();
		if (j + 1 < pLen && p[j + 1] == '*') {
			do {
				if (isMatch(s, p, i, j + 2)) return true;
			} while (i < sLen && (s[i++] == p[j] || '.' == p[j]));
		}
		else if (i < sLen && j < pLen && (s[i] == p[j] || '.' == p[j])) {
			return isMatch(s, p, i + 1, j + 1);
		}
		return i == sLen && j == pLen;
	}
};
