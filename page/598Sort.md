# 598.排序


题目描述
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。

小蓝最近学习了一些排序算法，其中冒泡排序让他印象深刻。

在冒泡排序中，每次只能交换相邻的两个元素。

小蓝发现，如果对一个字符串中的字符排序，只允许交换相邻的两个字符， 则在所有可能的排序方案中，冒泡排序的总交换次数是最少的。

例如，对于字符串 
lan 排序，只需要 
1
1 次交换。对于字符串 
qiao 排序，总共需要 
4
4 次交换。

小蓝找到了很多字符串试图排序，他恰巧碰到一个字符串，需要 
100
100 次交 换，可是他忘了吧这个字符串记下来，现在找不到了。

请帮助小蓝找一个只包含小写英文字母且没有字母重复出现的字符串，对 该串的字符排序，正好需要 
100
100 次交换。如果可能找到多个，请告诉小蓝最短的那个。如果最短的仍然有多个，请告诉小蓝字典序最小的那个。


```python
import os
import sys

# 请在此输入您的代码
sum_x = 0
i = 1
for i in range(1, 101):
  sum_x += i
  if sum_x >= 100:
    break
x = sum_x - 100
result = str()
sum_x = 0
first_letter = str()
for j in range(i, -1, -1):
  if i - j == x:
    first_letter = str(chr(97+j))
  else:
    result += str(chr(97+j))
print(first_letter + result)
```

