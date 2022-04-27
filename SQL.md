## 查询

```python
SELECT 字段1, 字段2 FROM 表名
SELECT `from` FROM 表名 # 如果使用关键字则在前后使用反引号
SELECT * FROM 表名 # *表示表内所有字段
SELECT DISTINCT 字段1 FROM 表名 # 去除重复，保留查询结果中重复内容（如果查询多个字段，表示保留独一无二的字段组合）


SELECT * FROM 表名 ORDER BY 字段1 # 按字段1从小到大排序（字段名可以用其在表中的列号表示）
SELECT * FROM 表名 ORDER BY 字段1 DESC # 按字段1从大到小排序
SELECT * FROM 表名 ORDER BY 字段1 DESC, 字段2, DESC # 按字段1从大到小排序，但相同的内容按字段2从大到小排序
SELECT * FROM 表名 ORDER BY 字段1 LIMIT 3 # 只显示查询结果中前3条记录
SELECT * FROM 表名 ORDER BY 字段1 LIMIT 1 OFFSET 2 # 跳过查询结果中前两行，只显示后面第1条记录


SELECT * FROM 表名 WHERE 字段1 <= XXX # 只对原始表格中满足where条件的记录中采取查询操作（<>或者!=表示不等于），where中可以引入逻辑运算符and, or, not，并且可以通过括号改变优先级（not > and > or）
SELECT * FROM 表名 WHERE 字段1 IS NULL # 存在缺失数据的记录
SELECT * FROM 表名 WHERE 字段1 IN (XXX, XXX, ...) # 限制字段在集合内，代替多个or
SELECT * FROM 表名 WHERE 字段1 LIKE %X% # 模糊查询，找到对应模板的记录，%通配符表示任意多个任意字符（使用转义字符\%，表示真实的%）
SELECT * FROM 表名 WHERE 字段1 LIKE __X # 模糊查询，找到对应模板的记录，一个_通配符表示一个任意字符


SELECT * FROM 表名 WHERE 字段1 - 字段2 > X # 数值型字段可以进行数学运算（但会影响查询效率）
SELECT *, 字段1 - 字段2 AS XXX FROM 表名 WHERE 字段1 - 字段2 > X ORDER BY XXX # 展示额外的字段列，并重给予别名，且在后续的操作（如order by）中可以使用前面命名的字段
SELECT *, CONCAT(字段1, '(', 字段2, ')') AS XXX FROM 表名 ORDER BY ABS(字段2) # 使用内置函数对字段进行操作，对于字符型字段可以使用concat进行组合构建新字段


SELECT * FROM 表名 WHERE 字段1 = '2022-01-01 20:00:00' # datetime类型以如期+时间的形式保存时间数据（2022-01-01 20:00:00）（也可以使用'2022/01/01 20:00:00'），如果只给出日期，则默认时间为'00:00:00'，
SELECT * FROM 表名 WHERE 字段1 >= '2022-01-01 00:00:00' AND 字段1 <= '2022-01-02 00:00:00' # 获取某天的记录
SELECT * FROM 表名 WHERE DATE(字段1) = '2022-01-01' # 获取某天的记录（但会影响查询效率），也可以使用YEAR、MONTH、DAY、HOUR、MINUTE、SECOND来锁定其他时间（如：DAY(字段1)=29表示每月的29号）
SELECT * FROM 表名 WHERE DATEDIFF(字段1 - 字段2) > XXX # 表示两个日期时间型字段之间相差的天数
SELECT * FROM 表名 WHERE 字段1 BETWEEN '2022-01-01 00:00:00' AND '2022-01-02 00:00:00' # 获取某个区间内数据


SELECT COUNT(字段1) FROM 表名 # 统计表内所有不是NULL的有效记录数量，可以使用COUNT(*)来统计
SELECT COUNT(*) AS 2022年4月总数 FROM 表名 WHERE YEAR(字段1) = 2022 AND MONTH(字段1) = 4 # 统计2022年9月的记录总数
SELECT COUNT(DISTINCT 字段1) FROM 表名 # 统计表内不同的有效字段1数量，不能使用COUNT(DISTINCT *)
SELECT SUM(字段1) FROM 表名 # 获取字段的总数，忽略NULL
SELECT AVG(字段1) FROM 表名 # 获取字段的均值，忽略NULL
SELECT MAX(字段1) FROM 表名 # 获取字段的最大值，忽略NULL
SELECT MIN(字段1) FROM 表名 # 获取字段的最小值，忽略NULL


SELECT 字段1, SUM(字段2) AS XXX FROM 表名 GROUP BY 字段1 ORDER BY XXX DESC # 按照字段1分组，并计算每个组内部的统计值（会单独对NULL进行分组），并进行排序
SELECT SUM(字段1) FROM 表名 GROUP BY 字段1, 字段2 # 嵌套分组，先按照字段1分组，然后对分组结果按照字段2分组，并计算每个组内部的统计值


SELECT SUM(字段1), 类别名X AS XXX FROM 表名 WHERE 字段2 = XXX GROUP BY 字段1 # 增加一列XXX字段均填充为类别名X
SELECT SUM(字段1) FROM 表名 GROUP BY 字段2 HAVING SUM(字段1) > XXX # 再group by的结果中，筛选统计值满足条件的记录，where用来筛选记录，having用来筛选分组
```
- SQL大小写不敏感，且可以自由换行书写，中英文都可以使用
- 执行顺序：from -> where -> group by（mysql可以放到select后面） -> having -> select（聚集函数） -> order by -> desc -> limit -> offset
- 书写顺序：select -> 字段名 -> from -> 表名 -> where -> group by -> having -> order by -> desc -> limit -> offset

