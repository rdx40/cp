class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
	    int closest = nums[0];
	    for (int num : nums){
		    if ((abs(num)<abs(closets)) || (abs(num) == abs(closest) && num>closest)){
			    closest = num;
		    }
	    }
	    return closest
};
