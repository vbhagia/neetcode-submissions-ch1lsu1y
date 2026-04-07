class Solution {
public:
    bool isAnagram(string s, string t) {
       /* Use a hash map to keep track of
        * count of each letter (for each s and t)
        * when done, if the hash maps are equal,
        * we have an anagram */ 
        if (s.length() != t.length()) {
            return false;
        }
        unordered_map<char, int> hashmap_s;
        unordered_map<char, int> hashmap_t;
        for (int i=0; i<s.length(); i++) {
            hashmap_s[s[i]]++;
            hashmap_t[t[i]]++;
        }
        return hashmap_s == hashmap_t;
    }
};
