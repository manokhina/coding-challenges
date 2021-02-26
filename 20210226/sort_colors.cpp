/*
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
*/

#include<vector>
#include<iostream>
#include<map>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        map<int, int> counter;
        int length = nums.size();
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                counter[0] += 1;
            } else if (nums[i] == 1) {
                counter[1] += 1;
            } else if (nums[i] == 2) {
                counter[2] += 1;
            }
        }
        vector<int>zeros(counter[0], 0);
        vector<int>ones(counter[1], 1);
        vector<int>twos(counter[2], 2);
        nums.clear();
        nums.reserve(length); // preallocate memory
        nums.insert( nums.end(), zeros.begin(), zeros.end() );
        nums.insert( nums.end(), ones.begin(), ones.end() );
        nums.insert( nums.end(), twos.begin(), twos.end() );  
    }
};

int main() {
  Solution s;
  vector<int> test = {0, 2, 1, 0};
  s.sortColors(test);
  for (auto i = 0; i < test.size(); i++ ) {
    cout << test[i] << endl;
  }
  return 0;
}