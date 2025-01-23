def can_partition_k_subsets(nums, k):
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False

    target = total_sum // k
    nums.sort(reverse=True)
    used = [False] * len(nums)

    def backtrack(start, k, current_sum):
        if k == 0:
            return True
        if current_sum == target:
            return backtrack(0, k - 1, 0)
        for i in range(start, len(nums)):
            if not used[i] and current_sum + nums[i] <= target:
                used[i] = True
                if backtrack(i + 1, k, current_sum + nums[i]):
                    return True
                used[i] = False
        return False

    return backtrack(0, k, 0)

# Example usage:
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(can_partition_k_subsets(nums, k))  # Output: True