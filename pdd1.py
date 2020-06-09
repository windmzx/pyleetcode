def minop(x):
    i=1
    while x > 1:
        x = x//2
        i+=1
    return i
if __name__ == "__main__":
    print(minop(926132445))