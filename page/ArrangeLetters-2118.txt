# 2118.排列字母

问题描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。

小蓝要把一个字符串中的字母按其在字母表中的顺序排列。

例如，LANQIAO 排列后为 AAILNOQ。

又如，GOODGOODSTUDYDAYDAYUP 排列后为 AADDDDDGGOOOOPSTUUYYY。

请问对于以下字符串，排列之后字符串是什么？

WHERETHEREISAWILLTHEREISAWAY

【解法1】冒泡排序

```python
import os
import sys

# 请在此输入您的代码
s = "WHERETHEREISAWILLTHEREISAWAY"
s = list(s)
for i in range(len(s)):
  for j in range(len(s) - i-1):
    if s[j] > s[j+1]:
      s[j], s[j+1] = s[j+1], s[j]
print("".join(s))
```