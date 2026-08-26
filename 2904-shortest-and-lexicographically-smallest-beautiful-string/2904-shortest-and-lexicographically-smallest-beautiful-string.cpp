class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {

        set<string> ans;

        for (int i = 0; i < s.size(); i++) {
            int count = 0;

            for (int j = i; j < s.size(); j++) {

                if (s[j] == '1')
                    count++;

                if (count == k) {
                    ans.insert(s.substr(i, j - i + 1));
                }

                if (count > k)
                    break;
            }
        }

        string result = "";

        for (string x : ans) {
            if (result == "" ||
                x.size() < result.size() ||
                (x.size() == result.size() && x < result)) {
                
                result = x;
            }
        }

        return result;
    }
};