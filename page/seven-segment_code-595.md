# 595.七段码

原题链接：
https://www.lanqiao.cn/problems/595/learning/?first_category_id=1&sort=students_count&second_category_id=3

【解法1】图的DFS深度优先搜索

```python
import os
import sys

# 请在此输入您的代码
"""
  a b c d e f g
a[1 1 0 0 0 1 0]
b[             ]
c[             ]
d[             ]
e[             ]
f[             ]
g[             ]
"""

def back_track(graph: list, visit: list, n: int, i: int) -> int:
  count = 1
  for x in range(n):
    if visit[x] != 1 and graph[i][x] != 0:
      visit[x] = 1
      count += back_track(graph, visit, n, x)
      visit[x] = 0
  return count

graph = [
  [1, 1, 0, 0, 0, 1, 0],
  [1, 1, 1, 0, 0, 0, 1],
  [0, 1, 1, 1, 0, 0, 1],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 1, 1],
  [0, 1, 1, 0, 1, 1, 1]
]

visit = [0 for _ in range(len(graph))]
count = back_track(graph, visit, len(graph), 0)
print(count // 2)

```


