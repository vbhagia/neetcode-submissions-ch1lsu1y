class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> output(2);
        unordered_map<int, int> seen;

        for (int i=0; i<nums.size(); i++) {
            if (seen.count(target - nums[i]) == 1) {
                output.at(0) = seen[target - nums[i]];
                output.at(1) = i;
                return output;
            }
            seen[nums[i]] = i;
        }
    }
};
