
#include <stdio.h>

int searchInsert(int *nums, int numsSize, int target)
{
    int i, j;

    for (i = numsSize - 1; i >= 0; i--) //循环从第2个元素开始
    {
        if (target == nums[i])
        {
            return i;
        }
        if (target > nums[i])
        {
            return i + 1;
        }
    }
    return 0;
}
int main()
{
    int nums[] = {1, 3, 5, 6};
    printf("%d", searchInsert(nums, 4, 7));
    return 0;
}

