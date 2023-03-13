# 1457.杨辉三角形

【解法1】只通过40%

```python
import os
import sys

# 请在此输入您的代码
x = int(input())
# ls = [[0 for _ in range(200)] for i in range(200)]
ls = list()

def find_first(ls):
  k = 0
  for i in range(44723):
    ls_sub = []
    for j in range(i+1):
      y = 0
      if j == 0 or j == i:
        y = 1
      else:
        y = ls[i - 1][j - 1] + ls[i - 1][j]
      k += 1
      if y == x:
        return k
      ls_sub.append(y)
    ls.append(ls_sub)
  return -1

print(find_first(ls))
```


