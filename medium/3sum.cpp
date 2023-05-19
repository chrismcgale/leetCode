#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    // Aprox 10x faster and less memory
    vector<vector<int>> threeSum(vector<int>& nums) 
    {
        vector<vector<int>> ret;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        // For easch element of the array check whether 2 elements sum to target - element
        for(int i = 0; i < n && nums[i] <= 0; ++i) {
            if(i > 0 and nums[i] == nums[i-1] ) continue;
            int j = i+1, k = n-1;
            while(j < k){ 
                if(nums[i] + nums[j] + nums[k] == 0){
                    ret.push_back({nums[i], nums[j], nums[k]});
                    // check duplicate 2 here
                    while(j < k and nums[j] == nums[j+1]) j++;
                    while(j < k and nums[k] == nums[k-1]) k--;
                    j++, k--;
                }
                else if(nums[i] + nums[j] + nums[k] < 0) j++;
                else k--;
            }
        }
        return ret;
    }

    void twoSum(vector<int>& nums, int i, vector<vector<int>> &ret) 
    {
        unordered_set<int> seen;
        for (int j = i + 1; j < nums.size(); j++) {
            int comp = -nums[i] - nums[j];
            if (seen.count(comp)) {
                ret.push_back({nums[i], comp, nums[j]});
                while (j + 1 < nums.size() && nums[j] == nums[j + 1]) {
                    ++j;
                }
            }
            seen.insert(nums[j]);
        }
    }

    // divide and conquer approach
    vector<vector<int>> threeSumDivideConquer(vector<int>& nums) 
    {
        vector<vector<int>> ret;
        sort(nums.begin(), nums.end());
        // For easch element of the array check whether 2 elements sum to target - element
        for(int i = 0; i < nums.size() && nums[i] <= 0; ++i) {
            if (i == 0 || nums[i - 1] != nums[i]) {
                twoSum(nums, i, ret);  
            }
        }
        return ret;
    }
};