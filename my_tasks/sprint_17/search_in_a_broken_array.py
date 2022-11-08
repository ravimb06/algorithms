# 74178203

def broken_search(nums, target) -> int:
    left = 0
    right = len(nums)-1
    while left <= right:
        mid_idx = (left+right)//2
        middle = nums[mid_idx]
        if middle == target:
            return mid_idx
        if nums[left] <= middle:
            if nums[left] <= target < middle:
                right = mid_idx-1
            else:
                left = mid_idx+1
        else:
            if middle <= target <= nums[right]:
                left = mid_idx+1
            else:
                right = mid_idx+1
    return -1
