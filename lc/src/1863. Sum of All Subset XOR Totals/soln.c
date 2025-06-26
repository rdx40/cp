int dfs(int* nums, int numsSize, int index, int currentXor){
    if(index == numsSize)
        return currentXor;
    
    int include = dfs(nums, numsSize, index+1, currentXor ^ nums[index]);
    int exclude = dfs(nums, numsSize, index+1, currentXor);

    return include + exclude;
}
int subsetXORSum(int* nums, int numsSize) {
    return dfs(nums, numsSize, 0, 0);   
}
