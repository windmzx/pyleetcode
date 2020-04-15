from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i, 0)+1
        tree = list(map.keys())

        def adjust_heap(start, end):
            left = start*2+1
            right = start*2+2
            if left < end and map[tree[left]] < map[tree[start]]:
                tree[left], tree[start] = tree[start], tree[left]
                adjust_heap(left, end)
            if right < end and map[tree[right]] < map[tree[start]]:
                tree[right], tree[start] = tree[start], tree[right]
                adjust_heap(right, end)
        for i in range(k//2-1,-1,-1):
            adjust_heap(i, k)
        for i in range(k, len(tree)):
            if map[tree[i]] > map[tree[0]]:
                tree[0] = tree[i]
                adjust_heap(0, k)
        return tree[:k]


if __name__ == "__main__":
    x = Solution()

    re = [6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0]


    res=x.topKFrequent(re,6)
    print(res)
