// https://leetcode.com/problems/palindrome-number/description/

class Solution {
public:
    bool isPalindrome(int x) {
        string str = to_string(x);
        int leng = str.size();
        int mid = str.size()/2;
        for(int i=0;i<mid;i++){
            if(str[i] != str[leng - 1 - i]){
                return false;
            }
        }
        return true;
    }
};
