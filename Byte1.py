def solution(n, dist, array):
    left = 0
    right = 2
    res = 0
    while left < n-2:
        while right < n and array[right]-array[left] <= dist:
            right += 1
        if right-1-left >= 2:
            num = right-left-1
            res += num*(num-1)//2
        left += 1
    return res


if __name__ == "__main__":
    print(solution(5, 19, [1 ,10 ,20 ,30, 50]))
