# 605.年号字串


【解法1】
````python
import os
import sys

# 请在此输入您的代码
x = 2019
# print(ord("A")) A: 65
w = 1
res = str()
while x > 0:
  # n = x % 27
  z = x % 26
  if z == 0:
    z = 26
  
  x = x - z
  x = x // 26
  res = chr(ord("A") + z - 1) + res

print(res)
````