class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int t = (nums1.size() + nums2.size()) / 2;
        vector<int> merge;
        int i = 0;
        int j = 0;
        while(i < nums1.size() || j < nums2.size()) {
            if( i + j == t ) break;
            if (i < nums1.size() && j < nums2.size()) {
                if(nums1[i] < nums2[j]){
                    merge.push_back(nums1[i]);
                    i++;
                } else {
                    merge.push_back(nums2[j]);
                    j++;
                }
            } else if (i < nums1.size()) {
                    merge.push_back(nums1[i]);
                    i++;
            } else {
                    merge.push_back(nums2[j]);
                    j++;  
            }
        }
        
        if (merge.size() % 2 == 0) return static_cast<float>((merge[t - 1] + merge[t])) / 2;
        return merge[t];
    } 
};
