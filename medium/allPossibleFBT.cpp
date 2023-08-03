class Solution {
public:
    unordered_map<int, vector<TreeNode*>> memo;
    vector<TreeNode*> allPossibleFBT(int n) {
        if (memo.find(n) == memo.end()) {
            vector<TreeNode*> ans;
            if (n == 1) {
                ans.push_back(new TreeNode(0));
            } else if (n % 2 == 1) {
                for (int i = 0; i < n; ++i) {
                    int j = n - 1 - i;
                    for (TreeNode* left: allPossibleFBT(i)) {
                        for (TreeNode* right : allPossibleFBT(j)) {
                            TreeNode* bns = new TreeNode(0);
                            bns->left = left;
                            bns->right = right;
                            ans.push_back(bns);
                        }
                    }
                }
            }
            memo[n] = ans;
            
        } 
        return memo[n];
    }
};