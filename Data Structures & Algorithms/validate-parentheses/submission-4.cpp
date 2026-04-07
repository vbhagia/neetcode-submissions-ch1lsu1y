class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        if (s.length()%2 == 1) {
            return false;
        }
        for (int i=0; i<s.length(); i++) {
            if (s[i] == ')') {
                if (stack.size() == 0) {
                    return false;
                }
                if (stack.back() != '(') {
                    return false;
                }
                stack.pop_back();
            }
            else if (s[i] == '}') {
                if (stack.size() == 0) {
                    return false;
                }
                if (stack.back() != '{') {
                    return false;
                }
                stack.pop_back();
            }
            else if (s[i] == ']') {
                if (stack.size() == 0) {
                    return false;
                }
                if (stack.back() != '[') {
                    return false;
                }
                stack.pop_back();
            }
            else {
                stack.push_back(s[i]);
            }
        }
        if (stack.size() != 0) {
            return false;
        }
        return true;
    }
};
