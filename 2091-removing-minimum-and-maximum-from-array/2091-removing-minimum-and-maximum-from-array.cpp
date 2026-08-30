class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();

        int minIdx = 0;
        int maxIdx = 0;

        // Find indices of minimum and maximum
        for (int i = 0; i < n; i++) {
            if (nums[i] < nums[minIdx])
                minIdx = i;

            if (nums[i] > nums[maxIdx])
                maxIdx = i;
        }

        // Make minIdx the smaller index
        if (minIdx > maxIdx)
            swap(minIdx, maxIdx);

        // Case 1: Remove both from left
        int left = maxIdx + 1;

        // Case 2: Remove both from right
        int right = n - minIdx;

        // Case 3: Remove min from left and max from right
        int both = (minIdx + 1) + (n - maxIdx);

        return min({left, right, both});
    }
};
