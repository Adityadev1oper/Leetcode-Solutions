class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();

        // Store indices for every value
        unordered_map<int, vector<int>> mp;

        for (int i = 0; i < n; i++) {
            mp[nums[i]].push_back(i);
        }

        vector<int> ans;

        for (int i : queries) {
            vector<int>& v = mp[nums[i]];

            // Only one occurrence
            if (v.size() == 1) {
                ans.push_back(-1);
                continue;
            }

            // Find position of i
            int pos = lower_bound(v.begin(), v.end(), i) - v.begin();

            int m = v.size();
            int best = n;

            // Next occurrence
            int next = v[(pos + 1) % m];

            // Previous occurrence
            int prev = v[(pos - 1 + m) % m];

            // Circular distance
            int d1 = abs(i - next);
            d1 = min(d1, n - d1);

            int d2 = abs(i - prev);
            d2 = min(d2, n - d2);

            best = min(d1, d2);

            ans.push_back(best);
        }

        return ans;
    }
};