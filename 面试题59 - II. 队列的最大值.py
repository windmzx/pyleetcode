# -*- encoding: utf-8 -*-
'''
@File    :   面试题59 - II. 队列的最大值.py
@Time    :   2020/05/09 11:41:43
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import queue

import queue


class MaxQueue:

    def __init__(self):
        self.maxqueue = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        if not self.maxqueue:
            return -1
        return self.maxqueue[0]

    def push_back(self, value: int) -> None:
        while self.maxqueue and self.maxqueue[-1] < value:
            self.maxqueue.pop()
        self.maxqueue.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        # Your MaxQueue object will be instantiated and called as such:
        # obj = MaxQueue()
        # param_1 = obj.max_value()
        # obj.push_back(value)
        # param_3 = obj.pop_front()
        if not self.maxqueue:
            return -1
        res = self.queue.get()
        if res == self.maxqueue[0]:
            self.maxqueue.popleft()


if __name__ == "__main__":
    x = MaxQueue()
    print(x.push_back(1))
    print(x.push_back(2))
    print(x.push_back(3))
    print(x.max_value())
    print(x.push_back(4))
    print(x.max_value())
    print(x.pop_front())
    print(x.max_value())
