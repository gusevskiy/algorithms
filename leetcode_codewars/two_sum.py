a = [2, 1, 3, 6]

# for i, s in enumerate(a):
#     print(i, s)


def two_sum(nums, target):
        idxs = dict()
        for idx, num in enumerate(nums):
            if (target - num) in idxs:
                return [idxs[target-num], idx]
            idxs[num] = idx
        return []
        
        
print(two_sum(a, 4))