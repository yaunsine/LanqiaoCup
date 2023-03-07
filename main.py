"""
    TODO: 转换markdown文件为pdf文件
    @author: yaunsine
    @date: 2023-03-07
"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
import time

from transferFile import *
import threading


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def grip_run(md_from=None) -> None:
    os.system("grip {0}".format(md_from))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    md_file_from = "result/result.md"
    pdf_file_to = "result/result.pdf"
    # grip_run(md_from=md_file_from)
    thread1 = threading.Thread(target=grip_run, args=(md_file_from, ))
    thread2 = threading.Thread(target=transfer, args=(pdf_file_to, ))
    # transfer(pdf_file_to)
    thread1.start()
    time.sleep(5)
    thread2.start()
    thread1.join()
    thread2.join()
    print("thread kill...")