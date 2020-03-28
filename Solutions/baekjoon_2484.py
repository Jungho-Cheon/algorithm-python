N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]

res = 0
for nums in arr:
    # set을 사용하면 중복을 찾을 수 있다.
    set_ = set(nums)
    nums.sort()
    # 모두 같은 경우
    if len(set_) == 1:
        res = max(res, 50000+(nums[0] * 5000))
    # (3,1), (2,2)
    elif len(set_) == 2:
        if nums[1] == nums[2]:
            res = max(res, 10000+(nums[1] * 1000))
        else:
            res = max(res, 2000+(nums[0] * 500)+(nums[3] * 500))
    # (2, 1, 1)
    elif len(set_) == 3:
        if nums[0] == nums[1]:
            res = max(res, 1000+(nums[0] * 100))
        elif nums[1] == nums[2]:
            res = max(res, 1000+(nums[1] * 100))
        else:
            res = max(res, 1000+(nums[2] * 100))
    # (1, 1, 1, 1)
    else:
        res = max(res, nums[3] * 100)
print(res)
