from typing import List
import copy


def main(n):
    source = [i+1 for i in range(n)]

    def helper(temp: List[int], source1: List[int]):
        if len(temp) == n:
            res.append(copy.deepcopy(temp))
        for i in range(len(source1)):
            if len(temp) > 0:
                num = source1[i]
                if abs(temp[-1]-num) > 1:
                    temp.append(num)
                    helper(temp, source1[:i]+source1[i+1:])
                    temp.pop()

            else:
                num = source1[i]
                temp.append(num)
                helper(temp, source1[:i]+source1[i+1:])
                temp.pop()
    res = []
    helper([], source)
    return res


if __name__ == "__main__":
    print(main(4))
