# 597.跑步训练



【超时解法】
```python
import os
import sys

# 判断是否闰年
def judge_leap_year(year) -> bool:
  if year % 400 == 0:
    return True
  if year % 100 != 0 and year % 4 == 0:
    return True
  return False

# 计算每年的天数
def calculate_days(year) -> int:
  if judge_leap_year(year):
    return 366
  else:
    return 365

# 计算每月的天数
def month_days(month, year=2020) -> int:
  big_m = [1, 3, 5, 7, 8, 10, 12]
  small_m = [4, 6, 9, 11]
  if month == 2:
    return 29 if judge_leap_year(year) else 28
  elif month in big_m:
    return 31
  elif month in small_m:
    return 30 

y = 2000
m = 1
d = 1
wd = 6
days_metres = 0

while y < 2020:
  if wd == 1 and d == 1:
    days_metres += 2
  elif wd == 1:
    days_metres += 2
  elif d == 1:
    days_metres += 2
  else:
    days_metres += 1
  
  d += 1
  wd += 1
  if wd > 7:
    wd = 1
  if month_days(m) > d:
    m += 1
    d = 1
  if m > 12:
    m = 1
    y += 1

while m < 10:
  if wd == 1 and d == 1:
    days_metres += 2
  elif wd == 1:
    days_metres += 2
  elif d == 1:
    days_metres += 2
  else:
    days_metres += 1
  
  d += 1
  wd += 1
  if wd > 7:
    wd = 1
  if month_days(m) > d:
    m += 1
    d = 1
  if m > 12:
    m = 1
    y += 1

while d <= 1:
  if wd == 1 and d == 1:
    days_metres += 2
  elif wd == 1:
    days_metres += 2
  elif d == 1:
    days_metres += 2
  else:
    days_metres += 1
  
  d += 1
  wd += 1
  if wd > 7:
    wd = 1
  if month_days(m) > d:
    m += 1
    d = 1
  if m > 12:
    m = 1
    y += 1
print(days_metres)


```

【算法2】

借助`datetime`库

```python
import os
import sys

import datetime

start = datetime.date(2000, 1, 1)
end = datetime.date(2020, 10, 1)
days = datetime.timedelta(days=1)
ans = 0

while start <= end:
  if start.day == 1 or start.weekday() == 0:
    ans += 2
  else:
    ans += 1
  start += days

print(ans)
```

【解法3】

暴力求解

```python
import os
import sys

def get_kilometres():
  months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  cnt = 0
  ans = 6
  for year in range(2000, 2021, 1):
    # 判断闰年
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      months[1] = 29
    else:
      months[1] = 28
    for i, m in enumerate(months):
      for d in range(1, m + 1, 1):
        cnt += 1
        if ans > 7:
          ans = 1 
        if ans == 1 or d == 1:
          cnt += 1
        ans += 1  # 星期更新
        if year == 2020 and i + 1 == 10 and d == 1:
          return cnt
print(get_kilometres())
```

