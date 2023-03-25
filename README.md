# 蓝桥杯2023
```
.____                           .__                _________               
|    |   _____    ____     _____|__|____    ____   \_   ___ \ __ ________  
|    |   \__  \  /    \   / ____/  \__  \  /  _ \  /    \  \/|  |  \____ \ 
|    |___ / __ \|   |  \ < <_|  |  |/ __ \(  <_> ) \     \___|  |  /  |_> >
|_______ (____  /___|  /  \__   |__(____  /\____/   \______  /____/|   __/ 
        \/    \/     \/      |__|       \/                 \/      |__|    
```

<p style="text-align: center">
    <img src="https://img.shields.io/badge/语言-python3.7-orange.svg" alt=""/>
    <img src="https://img.shields.io/badge/运行终端-Windows-yellow.svg" alt=""/>
    <img src="https://img.shields.io/badge/开源协议-MIT协议-green.svg" alt=""/>
</p>

[中文](readme-zh.md) | [English](readme-en.md)

### 序言
此项目以lanqiao刷题笔记为例，将所有markdown编写的md文档进行合并操作，最后转为pdf文档，简化了知识笔记产出的流程，可以极大满足汇总笔记的要求。使用线程异步，请求html数据，转换pdf文档。

### 刷题链接1：https://www.lanqiao.cn/cup/?sort=students_count&second_category_id=3

### 题库链接2：https://www.lanqiao.cn/problems/


## 笔记列表：

- [505.数字三角形](page/505NumberThreeAngle.md)

- [497.成绩分析](page/497Grade.md)

<details>
    
<summary><b>查看更多</b></summary>

- [598.排序](page/598Sort.md)

- [594.蛇形填数](page/SnakeFillin-594.md)

- [597.跑步锻炼](page/RunExercise-597.md)

- [646.等差素数列](page/IsochromaticPrimeSequence-646.md)

- [819.递增序列](page/IncrementalSequence-819.md)

- [604.组队](page/OrganizeATeam-604.md)

- [1643.货物摆放](page/GoodsPlacement-1463.md)

- [1445.空间](page/1445Space.md)

- [2080.求和](page/Sum-2080.md)

- [2060.裁纸刀](page/PaperCutter-2060.md)

- [595.七段码](page/seven-segment_code-595.md)

- [2381.三角回文数](page/TrianglePlindrome-2381.md)

- [1452.时间显示](page/TimeShow-1452.md)

- [2140.星期计算](page/WeeklyCalculation-2140.md)

- [595.七段码](page/seven-segment_code-595.md)

- [2118.字母排列](page/ArrangeLetters-2118.md)

- [2380.打卡](page/ClockIn-2380.md)

- [605.年号字串](page/YearString-605.md)
    
</details>







### 省赛时间：2023-04-08(周六)

本项目`Git Https`链接：
> https://github.com/yaunsine/LanqiaoCup.git


本项目`Git SSH`链接:
> git@github.com:yaunsine/LanqiaoCup.git


### 加载环境:
```shell
pip install -r requirements.txt
```

### 合并多个markdown
在`cmd`终端下运行
```shell
combine.bat
```

### markdown文件转pdf方法:
```shell
python main.py
```


### 第三方工具
[1] `wkhtmltopdf`工具

[2] `grip`工具


