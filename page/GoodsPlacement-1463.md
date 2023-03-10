# 1463.货物摆放问题

题目描述
小蓝有一个超大的仓库，可以摆放很多货物。

现在，小蓝有 
n 箱货物要摆放在仓库，每箱货物都是规则的正方体。小蓝规定了长、宽、高三个互相垂直的方向，每箱货物的边都必须严格平行于长、宽、高。

小蓝希望所有的货物最终摆成一个大的长方体。即在长、宽、高的方向上分别堆 
L、
W、
H 的货物,满足 
n=L×W×H。

给定 
n，请问有多少种堆放货物的方案满足要求。

例如，当 
n=4 时，有以下 
6
6 种方案：
1
×
1
×
4
、
1
×
2
×
2
、
1
×
4
×
1
、
2
×
1
×
2
、
2
×
2
×
1
、
4
×
1
×
1
1×1×4、1×2×2、1×4×1、2×1×2、2×2×1、4×1×1。

请问，当 
n=2021041820210418 （注意有 
16
16 位数字）时，总共有多少种方案？

提示：建议使用计算机编程解决问题。

答案提交
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。

运行限制
最大运行时间：1s
最大运行内存: 256M

【解法1】求因子列表，重新组合（需要在pycharm运行才能不超时）
```python
import os
import sys

# 请在此输入您的代码
# n = L * W * H 因式分解*3

"""
import os
import sys
# 请在此输入您的代码
# n = L * W * H 因式分解*3

ans = 0
n = 2021041820210418
factor_list = []
j = 0
ans = 0
for i in range(1, int(pow(n, 0.5))):
    if n % i == 0:
        factor_list.append(i)
        j = n // i  # n = i * j = i * (x * y) = (x * y) * j
        if j != i:
            factor_list.append(j)

print(len(factor_list))

for i in factor_list:
    for j in factor_list:
        for k in factor_list:
            if i * j * k == n:
                ans += 1

print(ans)
"""
print(2430)

```

【解法2】 大佬的解法，可以直接在蓝桥云平台运行

```python
import os
import sys
# 因素+背包（求因子）+遍历
# 不到50毫秒！！！！！！！！！！
# 请在此输入您的代码
n=2021041820210418
l=[]     # ！！！！用于存因数不是因子例如：10=2*5
i=2
x=n
while i<pow(x, 0.5):
    if x%i==0:
        l.append(i)
        x=x//i
    else:
        i+=1

l.append(x)
s={1}   # ！！！！用于存因子 如10=1*2*5*10
for j in l:
    s = set([j*k for k in s]) | s
count=0
for k1 in s:             # 遍历两层求解
    for k2 in s:
        if n%(k1*k2)==0:
            count+=1
print(count)
```



