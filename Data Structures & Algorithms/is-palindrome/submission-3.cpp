#include <cctype>
#include <string>
class Solution {
public:
    bool isPalindrome(string s) {
        /*We can take a 2 pointer approach
        * Start by taking a to the beginning of the string
        * And a pointer to the end the string
        * while the values at each are equal
        * move each pointer closer to the center and check again
        * Do this until the distance between the addresses is 1 or 0.
        */
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
                while (left < right && !alphaNum(s[left])) {
                    left++;
                }
                while (right > left && !alphaNum(s[right])) {
                    right--;
                }
                if (tolower(s[left]) != tolower(s[right])) {
                    return false;
                }
                left++;
                right--;
        }
        return true;
    }

    bool alphaNum(char c) {
        return (c >= 'A' && c <='Z' ||
                c >= 'a' && c <='z' ||
                c >= '0' && c <='9');
    }
};
