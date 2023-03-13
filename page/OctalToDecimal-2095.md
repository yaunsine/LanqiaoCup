# 2095.九进制转十进制

【解法1】调用python库的int方法
```python
print(int("2022", 9))
```

【解法2】常规解法
```python
import os
import sys

# 请在此输入您的代码
nine_x = 2022
ten_x = 0
w = 1
while nine_x != 0:
  ten_x = ten_x + nine_x % 10 * w
  nine_x = nine_x // 10
  w = w * 9

print(ten_x)
```


由此，可以得出n进制转10进制的代码:
```python3
def n_to_decimal(n_x, n) -> int:
  w = 1
  ten_x = ten_x + nice_x % 10 * w
  n_x = n_x // 10
  w = w * n
  return ten_x
```



