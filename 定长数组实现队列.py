# -*- encoding: utf-8 -*-
'''
@File    :   定长数组实现队列.py
@Time    :   2020/06/08 17:47:40
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class MyQueue:

    def __init__(self, size):
        super().__init__()
        self.head = 0
        self.tail = 0
        self.size = 0
        self.cap = size
        self.array = [0 for i in range(size)]

    def add(self, num):
        if self.size >= self.cap:
            raise Exception("no space")
        else:
            self.array[self.tail] = num
            self.size += 1
            self.tail = (self.tail+1) % self.cap

    def addhead(self, num):
        if self.size >= self.cap:
            raise Exception("no space")
        else:
            self.array[self.head-1] = num
            self.size += 1
            self.head -= 1
            if self.head < 0:
                self.head = self.head+self.cap

    def lpop(self):
        if self.size <= 0:
            raise Exception("no enough money")
        else:
            num = self.array[self.head]
            self.head = (self.head+1) % self.cap
            self.size -= 1
            return num

    def rpop(self):
        if self.size <= 0:
            raise Exception("no enough money")
        else:
            num = self.array[self.tail-1]
            self.tail -= 1
            if self.tail < 0:
                self.tail += self.cap
            self.size -= 1
            return num


if __name__ == "__main__":
    x = MyQueue(3)
    x.add(1)
    x.add(2)
    x.addhead(3)
    print(x.lpop())
    print(x.rpop())
    x.add(4)
    x.lpop()
    x.add(5)
    x.lpop()
    x.add(6)
    x.lpop()
    print(x)
