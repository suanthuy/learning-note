class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target){
            int length = nums.size();
            unordered_map<int, int> numsMap;

            for(int i=0;i<length;i++){
                int complement = target - nums[i];
                numsMap[complement] = i;
            }
            for(int i=0;i<length;i++){
                if(numsMap.count(nums[i]) && numsMap[nums[i]] != i)
                        return {i, numsMap[nums[i]]};
            }
            return {};
        }
       
};

