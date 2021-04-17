/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <stdio.h>
int *sortedSquares(int *A, int ASize, int *returnSize)
{
    int i, j, t, *returnArr, flag = 0;
    *returnSize = ASize;
    returnArr = (int *)malloc(ASize * sizeof(int));
    returnArr[0] = A[0] * A[0];
    for (i = 1; i < ASize; i++)
    {

        t = A[i] * A[i];
        for (j =i-1; j >=0; j--)
        {
            if (t < returnArr[j])
            {
                returnArr[j+1] = returnArr[j];
            }
            else
                break;
        }
        returnArr[j+1] = t;
    }

    return returnArr;
}
int main()
{
    int arr[] = {1,2,4,2,1};
    int size = sizeof(arr) / sizeof(int);
    int i, *arr2;
    arr2 = sortedSquares(arr, size, &size);
    for (i = 0; i < size; i++)
    {
        printf("%d ", arr2[i]);
    }
}