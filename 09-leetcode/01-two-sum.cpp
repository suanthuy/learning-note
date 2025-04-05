// https://leetcode.com/problems/two-sum/description/
// :%y+

/* Method 1.1: Brute Force {{{ */
class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target){
            int leng=nums.size();
            for(int i=0;i<leng-1;i++){
                for(int j=leng-1;j>i;j--){
                    if(nums[i] + nums[j] == target){
                        return {i,j};
                    }
                }
            }
            return {};
        }
}
/* }}} */

/* Method 1.2: Brute Force {{{ */
class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target){
            int leng=nums.size();
            for(int i=0;i<leng;i++){
                for(int j=i+1;j<leng;j++){
                    if(nums[i] + nums[j] == target){
                        return {i,j};
                    }
                }
            }
            return {};
        }
}
/* }}} */

// Method 2.1: Two pass Hash table
// Using Two pass Hash is very fast
class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> numMap;
            int leng = nums.size();
            // Build the hash table
            for(int i=0;i<leng;i++){
                numMap[nums[i]] = i;
            }

            // Find the complement
            for(int i=0;i<leng;i++){
                int complement = target - nums[i];
                // Check the complement in the list or not
                // Check complement cannot be itself, have to another number, not the same number
                if(numMap.count(complement) && numMap[complement] != i){
                    return {i, numMap[complement]};
                }
            }
            return {};
        }
};


// Method 2.2: Two pass Hash table
// Using Two pass Hash is very fast
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

// Method 3: One pass hash table
class Solution {
    public:
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int, int> numMap;
        int leng = nums.size();

        // Check complement in numMap
        for(int i=0;i<leng;i++){
            int complement = target - nums[i];
            if(numMap.count(complement)){
                return {numMap[complement], i};
            }
            // numMap[complement] = i // wrong
            numMap[nums[i]] = i;
        }
        return {};
    }
};




