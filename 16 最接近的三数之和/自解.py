class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        # 双指针法, 不过是15题的变体罢了
        n_nums = len(nums)
        if n_nums < 3: return []

        # 从小到大排序
        nums.sort()
        result = None
        last_num = None
        for cur in range(0, n_nums - 2):
            if nums[cur] == last_num: continue
            last_num = nums[cur]

            cur_left = cur + 1
            cur_right = n_nums - 1
            while cur_left < cur_right:
                num_sum = nums[cur] + nums[cur_left] + nums[cur_right] - target

                if num_sum == 0:
                    return target
                elif num_sum < 0:
                    if result is None or abs(num_sum) < abs(result):
                        result = num_sum
                    cur_left += 1
                else:
                    if result is None or abs(num_sum) < abs(result):
                        result = num_sum
                    cur_right -= 1
 
        return result + target