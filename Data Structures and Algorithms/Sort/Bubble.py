
def bubble_sort(li):
    n = len(li)
    for i in range(n- 1): # 第i趟
        exchange = False # 如果一趟排序无交换，则可认为已经排好序了
        for j in range(n - i - 1):
            if li[j] > li[j - 1]: # 每次对比相邻两个数，如果前面比后面大，则交换这两个数（降序li[j] < li[j - 1]）
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return

if __name__ == '__main__':
    import random
    li = [random.randint(0, 100) for i in range(10)]
    print(li)
    bubble_sort(li)
    print(li)