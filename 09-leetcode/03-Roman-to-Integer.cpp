// https://leetcode.com/problems/roman-to-integer/description/

class Solution {
    public:
        int charToInt(char a){
            switch(a){
                case 'I': return 1;
                case 'V': return 5;
                case 'X': return 10;
                case 'L': return 50;
                case 'C': return 100;
                case 'D': return 500;
                case 'M': return 1000;
                default: return 0;
            }
        }

        int romanToInt(string s) {
            int result = 0;
            for(int i=0;i<s.size();i++){
                if((s[i] == 'I')&&(s[i+1]=='V')){
                    result += 4;
                    i += 1;
                    continue;
                }
                else if((s[i] == 'I')&&(s[i+1]=='X')){
                    result += 9;
                    i += 1;
                    continue;
                }
                else if((s[i] == 'X')&&(s[i+1]=='L')){
                    result += 40;
                    i += 1;
                    continue;
                }
                else if((s[i] == 'X')&&(s[i+1]=='C')){
                    result += 90;
                    i += 1;
                    continue;
                }
                else if((s[i] == 'C')&&(s[i+1]=='D')){
                    result += 400;
                    i += 1;
                    continue;
                }
                else if((s[i] == 'C')&&(s[i+1]=='M')){
                    result += 900;
                    i += 1;
                    continue;
                }
                result += charToInt(s[i]);
            }
            return result;
        }
};
