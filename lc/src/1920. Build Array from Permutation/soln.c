int* buildArray(int* nums, int numsSize, int* returnSize) {
    int *ans = (int *)malloc(numsSize*sizeof(int));
    *returnSize = numsSize;
    for(int i=0;i<numsSize;i++){
        ans[i] = nums[nums[i]];
    }
    return ans;
}
