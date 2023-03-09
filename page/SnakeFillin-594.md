# 594.蛇形填数

题目描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。

如下图所示，小明用从 
1 开始的正整数“蛇形”填充无限大的矩阵。

```shell
1 2 6 7 15 ...
3 5 8 14 ...
4 9 13 ...
10 12 ...
11 ...
...
```

容易看出矩阵第二行第二列中的数是 
5。请你计算矩阵中第
20 行第 
20 列的数是多少？

【解法1】

模拟动态规划

```python
import os
import sys

mat = [[0 for _ in range(200)] for _ in range(200)]

i = 0
j = 0
mat[i][j] = 1
cnt = 1
while mat[19][19] == 0:
  # 右移
  j += 1
  cnt += 1
  mat[i][j] =  cnt
  # 左下角
  while j != 0:
    i += 1
    j -= 1
    cnt += 1
    mat[i][j] = mat[i][j]
  # 下移
  i += 1
  cnt += 1
  mat[i][j] = cnt
  # 右上角
  while i != 0:
    i -= 1
    j += 1
    cnt += 1
    mat[i][j] = cnt

print(mat[19][19])
```

【解法2】

对角线计算法

```python
res = 1
for i in range(0, 20, 1):
    res += i * 4
print(res)
```

