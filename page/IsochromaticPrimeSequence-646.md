# 646.等差素数列

【解法1】暴力解法

```python
import os
import sys

# 请在此输入您的代码
# i + 0x, i + x, i + 2x, i + 3x, i + 4x, i + 5x, i + 6x, ..., i + 9x
def is_prime(x) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def tolerance() -> int:
    # 初始值
    for i in range(2, 1001):
        # 公差
        for j in range(2, 1001):
            k = 0
            for k in range(10):
                if is_prime(i + j * k):
                    continue
                else:
                    break
            if k == 9:
                return j
    return -1


print(tolerance())
```


