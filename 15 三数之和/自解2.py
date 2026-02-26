class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 双指针法
        n_nums = len(nums)
        if n_nums < 3: return []

        # 从小到大排序
        nums.sort()
        results = []
        last_num = None
        for cur in range(0, n_nums - 2):
            if nums[cur] == last_num: continue
            last_num = nums[cur]

            cur_left = cur + 1
            cur_right = n_nums - 1
            while cur_left < cur_right:
                num_sum = nums[cur] + nums[cur_left] + nums[cur_right]
                if num_sum == 0:
                    results.append([nums[cur], nums[cur_left], nums[cur_right]])
                    cur_left += 1
                    cur_right -= 1
                    while cur_left < cur_right and nums[cur_left] == nums[cur_left - 1]:
                        cur_left += 1
                    while cur_left < cur_right and nums[cur_right] == nums[cur_right + 1]:
                        cur_right -= 1
                elif num_sum < 0:
                    cur_left += 1
                else:
                    cur_right -= 1
        return results