## 复杂度

n是问题规模

- 时间复杂度：评估算法时间占用的方式
  - 简单结构：O(1)
  - 循环减半：O(logn)
  - 单层循环：O(n)
  - k层循环：O(n^k)
- 空间复杂度：评估算法内存占用大小的方式
  - 可数变量：O(1)
  - 长度为n的一维列表：O(n)
  - m行n列的二维列表：O(mn)



## 递归

- 特点
  - 调用自身
  - 结束条件
- 汉诺塔问题：
  - n个盘子：
    - 上面n-1个圆盘从A经过C移动到B
    - 最下面第n个圆盘从A移动到C
    - n-1个圆盘从B经过A移动到C

```python
def hanoi(n, A, B, C):
    '''
    :param n: 盘子数量
    :param A: 第一个柱子
    :param B: 第二个柱子
    :param C: 第三个柱子
    :return:
    '''
    if n > 0:
        hanoi(n - 1, A, C, B) # 上面n-1个圆盘从A经过C移动到B
        print(f'moving from {A} to {C}') # 最下面第n个圆盘从A移动到C
        hanoi(n - 1, B, A, C)  # n-1个圆盘从B经过A移动到C

if __name__ == '__main__':
    hanoi(3, 'A', 'B', 'C')
```



## 查找

- 在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程
- index()：线性查找（列表不一定有序）
- 顺序查找O(n)：线性查找，遍历列表查找元素
- 二分查找O(logn)：从**有序列表**中，每次将待查找值与候选区中间值进行比较，使得候选区每次减半

```python
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
```

  

## 排序

- 将无序列表变成有序列表
- 时间复杂度O(n^2)：
  - 冒泡排序（Bubble Sort）：
    - 每两个相邻数，如果前面比后面大，则交换这两个数
    - 一趟操作完成后，无序区减少一个数，即当前无序区最后一个数加入有序区
    - 如果一趟排序无交换，则可认为已经排好序了
  - 选择排序（Select Sort）：
    - 每次将无序区最小的元素找出来，然后与无序区第一个元素交换，将其加入有序区
  - 插入排序（Insert Sort）：
    - 初始时有序区有一个数
    - 每次从无序区获取一个数，插入到有序区正确的位置（通过移动有序区元素位置来实现）

