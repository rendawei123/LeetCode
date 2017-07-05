

def single_number(nums):
    res = 0
    for i in nums:
        res ^= i
    return res

if __name__ == '__main__':
    l = [1, 1, 2, 3, 2]
    print(single_number(l))