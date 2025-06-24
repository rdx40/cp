class Solution {
public:
    bool isPalindrome(ListNode* head) {
        std::vector<int> vals;
        
        while (head) {
            vals.push_back(head->val);
            head = head->next;
        }

        int left = 0, right = vals.size() - 1;
        while (left < right) {
            if (vals[left] != vals[right])
                return false;
            left++;
            right--;
        }

        return true;
    }
};
