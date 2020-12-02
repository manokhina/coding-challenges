/*
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
*/
#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unsigned int num_pairs = 0;
        if (nums.size() < 2) {
            return num_pairs;
        }
        typedef map<unsigned int, unsigned int> CounterMap;
        CounterMap counts;
        for (int i = 0; i < nums.size(); ++i) {
            CounterMap::iterator it(counts.find(nums[i]));
            if (it != counts.end()) {
            it->second++;
            } else {
                counts[nums[i]] = 1;
            }
        }
        for (auto val : counts) {
            if (val.second > 1) {
                num_pairs += combinations(val.second);
            }
        }
        return num_pairs;
    }

private:
    int combinations(unsigned int n) {
        return n * (n - 1) / 2;
    }
};