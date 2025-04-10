---
title: python场景方案解决
data: 2025-4-3
---

# 拿到控制台所有输出

我这里是自己解析了命令, 暂时没有找到很好的库, 我这里解析的也不全

```python
import os
import sys
from tqdm import tqdm
import logging
import atexit

class ParseConsoleStr:
    def __init__(self):
        self.buffer = []
        self.current_line = ""
        

    def parse(self, text):
        for char in text:
            if char == "\r":
                self.current_line = ""  # 回车后重置当前行
            elif char == "\b":
                self.current_line = self.current_line[:-1]  # 退格删除最后一个字符
            else:
                self.current_line += char
        if "\n" in text:
            self.buffer.append(self.current_line.rstrip())  # 存入最终结果
            self.current_line = ""

    def get_output(self):
        return "\n".join(self.buffer) + ("\n" + self.current_line if self.current_line else "")


class ConsoleCapture:
    def __init__(self, output_file="output1.txt"):
      
        
        self.output_file = open(output_file, "w")
        self.parse = ParseConsoleStr()
        atexit.register(self.cleanup)

    def cleanup(self):
        self.output_file.write(self.parse.get_output())
        self.output_file.close()

        sys.stdout = sys.__stdout__  # 还原 stdout
        sys.stderr = sys.__stderr__  # 还原 stderr

    def write(self, text):
        sys.__stdout__.write(text)  # 输出到原始 stdout
        self.parse.parse(text)

    def flush(self):
        pass  # 不做任何处理


# 绑定到 sys.stdout
sys.stdout = ConsoleCapture()
sys.stderr = sys.stdout



import time
for i in tqdm(range(10)):
    time.sleep(0.1)

```

