
def insert_sort(li):
    n = len(li)
    for i in range(1, n): # i表示需要插入的元素下标
        tmp = li[i]
        j = i - 1 # 有序区元素下标
        while j >= 0 and li[j] > tmp: # 当有序区当前元素小于需要插入的元素，或达到有序区最左侧，停止移动，将该元素放在当前位置
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


if __name__ == '__main__':
    import random
    li = [random.randint(0, 100) for i in range(10)]
    print(li)
    insert_sort(li)
    print(li)