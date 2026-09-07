class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        unordered_map<int, vector<int>> mp;
        
        for (int i = 0; i < nums.size(); i++) {
            mp[nums[i]].push_back(i);
        }

        int ans = INT_MAX;

        for (auto &[value, pos] : mp) {
            for (int i = 0; i + 2 < pos.size(); i++) {
                int left = pos[i];
                int right = pos[i + 2];

                int dist = 2 * (right - left);

                ans = min(ans, dist);
            }
        }

        return ans == INT_MAX ? -1 : ans;
    }
};