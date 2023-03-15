# 2381.回文三角数

【解法1】

```python
import os
import sys
import math

# 请在此输入您的代码
"""
k(k+1) = k^2+k+1/4-1/4=(k+1/2)^2-1/4

n = k(k+1)/2
2n = k(k+1) = (k+1/2)^2-1/4
sqrt(2n+1/4)-1/2
"""
x = 20220514

# 判断回文
def is_palindrome(x: int) -> bool:
  x = str(x)
  i = 0
  j = len(x) - 1
  while i < j:
    if x[i] != x[j]:
      return False
    i += 1
    j -= 1
  return True


k = int(math.sqrt(2 * x + 0.25) - 0.5)

while k * (k + 1) // 2 <= x:
  k += 1
while True:
  res = k * (k + 1) // 2
  if is_palindrome(res):
    print(res)
    break
  k += 1
```