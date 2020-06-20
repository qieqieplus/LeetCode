class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& A) {
        int peek = A[0], result = 0;
        for (int i = 1; i < A.size(); ++i) {
            --peek;
            result = max(result, A[i] + peek);
            peek = max(peek, A[i]);
        }
        return result;
    }
};
