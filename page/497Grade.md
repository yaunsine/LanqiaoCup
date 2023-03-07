# 497.成绩分析

题目描述
小蓝给学生们组织了一场考试，卷面总分为 100 分，每个学生的得分都是一个 0 到 100 的整数。

请计算这次考试的最高分、最低分和平均分。

输入描述
输入的第一行包含一个整数
n (1≤n≤10 
4
 )，表示考试人数。

接下来 
n 行，每行包含一个 0 至 100 的整数，表示一个学生的得分。

输出描述
输出三行。

第一行包含一个整数，表示最高分。

第二行包含一个整数，表示最低分。

第三行包含一个实数，四舍五入保留正好两位小数，表示平均分。

输入输出样例
示例
输入

7
80
92
56
74
88
99
10
copy
输出

99
10
71.29

```python
import os
import sys

# 请在此输入您的代码
n = int(input())  # 考试人数
sum_score = 0   # 总分
max_score = 0   # 最高分
min_score = 0   # 最低分
for i in range(n):
  score = int(input())  # 考试得分
  if i == 0:
    min_score = score
  if min_score > score:
    min_score = score
  if max_score < score:
    max_score = score
  sum_score += score

print(max_score)
print(min_score)
print("%.2f"%(sum_score / n))
```

此题注意细节

