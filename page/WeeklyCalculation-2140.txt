# 2140.星期计算


原题：
https://www.lanqiao.cn/problems/2140/learning/?first_category_id=1&sort=students_count&second_category_id=3&tags=2022


问题描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。

已知今天是星期六，请问 20^{22}天后是星期几?

注意用数字 11 到 77 表示星期一到星期日。

【解法1】
```python
import os
import sys

# 请在此输入您的代码
cur = 6
fut = int(pow(20, 22) % 7)
fut = (fut + 6 - 1) % 7 + 1
print(fut)
```

【解法2】不使用pow()函数
```python
import os
import sys

# 请在此输入您的代码
cur = 6
days = 1
for i in range(22):
  days *= 20
fut = int(days % 7)
fut = (fut + 6 - 1) % 7 + 1
print(fut)
```



