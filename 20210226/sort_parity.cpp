/*
https://leetcode.com/problems/sort-array-by-parity-ii/

Given an array A of non-negative integers, half of the integers in A are odd, 
and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
*/
#include <vector>
#include <iostream>
#include <stack> 
using namespace std;

class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        stack<int> even;
        stack<int> odd;
        int length = A.size();
        vector<int> result;
        for (auto i = 0; i < length; i++) {
            if (A[i] % 2 == 1) {
                odd.push(A[i]);
            } else {
                even.push(A[i]);
            }
        }
        for (auto i = 0; i < length; i++) {
          if (i % 2 == 0) {
            result.push_back(even.top());
            even.pop();
          } else {
            result.push_back(odd.top());
            odd.pop();
          }
        }
        return result;
    }
};
