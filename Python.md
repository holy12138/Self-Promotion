## 基础：

- 逻辑运算符优先级：not > and > or

  

## 书写格式：

- 不同设置下tab可能表示不同数量的空格缩进



## 数据结构：

- 变量：
  - 变量名记录对应的值在内存中的地址索引
  - 判断是否为数字：`a.isnumeric()`
  - 布尔型变量True/False，是整数型变量的一个子类
  - 判断变量类型：
    - type：`x = type(a).__name__`
    - isinstance：`isinstance(a, int)`
  - 全局变量：在函数里引入`global x`，表示在该函数内可以对全局变量x进行更改
- 容器：
  - x[:]创建新list
  - a + [4]或者a + [1, 2, 3 ]会创建新列表，使用append和extend节约内存
  - x[8: 3: -1]表示以8为起始，4为结束，反向索引
  - 字典更改键'a' -> 'b'：`d['b'] = d.pop('a')`
- 数值：
  - 64位系统表示可以一次处理64个bit的数据，所以一般使用64个来bit（8个byte）表示一个数字（计算机最少1个byte用于存储一个数字，包含8个bit），python3中都是长整数
  - 四舍五入：
    - 银行家舍入法：round四舍五入，在5的位置奇数进位，偶数退位（但round受限于二进制，有时奇数遇到后续的5也会退位）
    - 显示小数：`format(x, '0.2f')`
  - //取余数：得到小于真实值的最大整数
    - 7 // 2 = 3
    - -7 // 2 = -4
- 




## 文件操作：

- r读取，w写入，a添加
- 文件夹下一层级所有文件名：`os.listdir(XXX)`
- 遍历文件夹中所有文件名：`os.walk(XXX)` -> [当前节点文件夹，[当前目录下子文件夹]，[当前目录下文件]]
- 文件重命名：`os.rename(原路径名，新路径名)`
- 操作结束后自动关闭文件：`with open(XXX, encoding='utf-8') as f:`



## 函数：

- 传参：
  - 必选参数、可选参数（有默认值）、不定长参数（单星号）、不定长关键字参数（双星号）
  - 不定长参数：
    - `*x`表示将传入的多个无关键字参数自动组成一个tuple（也可以直接传一个tuple）
    - `**x`表示将传入的多个带关键字参数自动组成一个字典（也可以直接传一个字典）



## 模块：

- 安装：`pip install -i 镜像网址 模块名`
- `__name__`在该文件被独立允许时为`__main__`，被其他文件调用时为当前文件的名字（每个py程序都会被当作Module类来运行，其都有一个`__name__`属性表示自己的名字，`__file__`表示该程序的存储路径）



## 异常处理：

- ```python
  try: # 尝试运行如下操作
  	XXX
  except FileNotFoundError:# 可以执行多个except
      print('文件不存在！')
  except Exception as e: 
      print('出现未知错误', e) # 查看错误类型
  else: # 没出现异常则执行
      print('没出现异常')
  finally: # 必须执行的操作
      print('程序执行结束')
  ```

- 



## 爬虫

- 启动浏览器窗口：`from urllib.request import urlopen`
- 获取网页反馈对象：`r = urlopen(XXX)`
- 获取网页内容：`c = r.read().decode('utf-8')`
- `<tr>与<\tr>之间`表示表格的每一行
- `<td>与<\td>之间`表示表格的每一列
- 使用BeautifulSoup：
  - `from bs4 import BeautifulSoup`
  - `bs_obj = BeautifulSoup(c, features='lxml')`
  - 获取表格：`t = bs_obj.find_all('table')`
  - 获取所有行：`all_tr = t.find_all('tr')`
