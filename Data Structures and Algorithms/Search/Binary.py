
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right: # 候选去有值
        mid = left + (right - left) // 2
        if li[mid] == val: # 找到该值，直接返回
            return mid
        elif li[mid] > val: # 待查找值在mid左侧，将right指向mid左侧第一个元素
            right -= 1
        else: # li[mid] < val，待查找值在mid右侧，将left指向mid右侧第一个元素
            left += 1
    else:
        return None

if __name__ == '__main__':
    li = list(range(1, 10))
    val = 3
    res = binary_search(li, val)
    print(res)