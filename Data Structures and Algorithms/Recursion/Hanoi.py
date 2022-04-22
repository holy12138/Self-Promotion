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