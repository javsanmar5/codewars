def repeats(arr: list) -> int:
    res = 0
    for i in arr:
        if arr.count(i) == 1:
            res += i

    return res



def repeats_one_line(arr: list) -> int:
    return sum([i for i in arr if arr.count(i) == 1])



arr = [1,1,2,3,4,3]

print(repeats(arr))
print(repeats_one_line(arr))