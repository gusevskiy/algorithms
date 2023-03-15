

def broken_search(nums, target) -> int:


    square1 = {nums[x] : x for x in range(len(nums)) } 
    
    if target in square1:
        return square1[target]
    return -1



def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


