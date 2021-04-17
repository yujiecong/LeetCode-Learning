
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            mid = low + (high - low) // 2 #防止 越界
            if numbers[mid] < numbers[high]:
                high = mid
            elif numbers[mid] > numbers[high]:
                low = mid + 1
            else:
                high -= 1
        return numbers[low]
