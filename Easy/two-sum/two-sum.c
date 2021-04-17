
#include <stdio.h>
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    int i, j,*returnArr;
    *returnSize=2;
    returnArr=(int *)malloc(sizeof(int)*2);
    for (i = 0; i < numsSize - 1; i++)
    {
        for (j = i+1; j < numsSize; j++)
        {
            if(nums[i]+nums[j]==target){
     
                *returnArr++=i;
                *returnArr--=j;
                return returnArr;
            }
        }
    }
    return NULL;
}