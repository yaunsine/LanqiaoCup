# 505数字三角形问题


![](https://doc.shiyanlou.com/courses/uid1580206-20210224-1614154063705)

上图给出了一个数字三角形。从三角形的顶部到底部有很多条不同的路径。对于每条路径，把路径上面的数加起来可以得到一个和，你的任务就是找到最大的和。

路径上的每一步只能从一个数走到下一层和它最近的左边的那个数或者右 边的那个数。此外，向左下走的次数与向右下走的次数相差不能超过 1。

输入描述
输入的第一行包含一个整数 
N
 
(
1
≤
N
≤
100
)
N (1≤N≤100)，表示三角形的行数。

下面的
N 行给出数字三角形。数字三角形上的数都是 0 至 100 之间的整数。

输出描述
输出一个整数，表示答案。

输入输出样例
示例
输入
```
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
```


输出
> 27

代码实现：
```python
import os
import sys

# 请在此输入您的代码
n = int(input())
i = 1
all_ls = list()
while i <= n:
  line = input()
  row_ls = line.split()
  row_ls = list(map(int, row_ls))
  all_ls.append(row_ls)
  i += 1


for i in range(1, n):
  for j in range(0, i + 1):
    if j == 0:
      all_ls[i][j] += all_ls[i - 1][j]
    elif j == i:
      all_ls[i][j] += all_ls[i - 1][j - 1]
    else:
      all_ls[i][j] += max(all_ls[i - 1][j - 1], all_ls[i - 1][j])

print(max(all_ls[-1][n // 2 - 1], all_ls[-1][n // 2]))
```

