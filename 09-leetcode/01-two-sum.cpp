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


