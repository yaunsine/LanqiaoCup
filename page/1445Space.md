# 1445.空间

本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。

小蓝准备用
256MB 的内存空间开一个数组，数组的每个元素都是 
32 位 二进制整数，如果不考虑程序占用的空间和维护内存需要的辅助空间，请问 
256MB 的空间可以存储多少个 
32 位二进制整数？

```python
import os
import sys

# 请在此输入您的代码
print(256 * 1024 * 1024 * 8 // 32)
```

