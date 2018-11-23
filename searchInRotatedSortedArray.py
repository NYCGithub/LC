class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        The array will always have 2 increasing segments. First segment's every element is larger than 2nd segment.
        Binary Search around a mid point in the whole array, then detremine if target is in the first and 2nd segment.

        Time: O(logN)
        Space: O(1)
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[end]:
                # Middle point is in the first increasing segment.
                # >= nums[end] is to handle when there's only 1 element left.
                if nums[mid] > target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[end]: # Middle point is in the 2nd increasing segment
                if nums[end] <= target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
