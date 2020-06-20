#include <cmath>
#include <algorithm>
#include <numeric>

class Solution {
public:
    int findBestValue(vector<int>& arr, int target) {
        sort(arr.begin(), arr.end());
        return findBestValue(arr.begin(), arr.end(), target);
    }

    int findBestValue(vector<int>::iterator start, vector<int>::iterator end, int target) {
        int avg = ceil(target*1.0 / (end - start) - 0.5);
        if (avg <= *start) {
            return avg;
        } else if (avg >= *prev(end)) {
            return *prev(end);
        } else {
            auto next = start;
            while(*next <= avg) {
                next++;
            }
            auto sum = accumulate(start, next, 0);
            return findBestValue(next, end, target - sum);
        }
    }
};
