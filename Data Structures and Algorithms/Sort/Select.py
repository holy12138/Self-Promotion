
def select_sort(li):
    n = len(li)
    for i in range(n - 1): # i是第几趟
        min_loc = i # 记录无序区最小数位置
        for j in range(i + 1, n): # 寻找无序区最小数
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

if __name__ == '__main__':
    import random
    li = [random.randint(0, 100) for i in range(10)]
    print(li)
    select_sort(li)
    print(li)