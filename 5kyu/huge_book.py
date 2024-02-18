def page_digits(summary: int) -> int:
    m = len(str(summary)) 
    base = 9 * (m-1) * (10**(m-2))
    extra = summary - (10**(m-2))

    return base + aux(extra)


def aux(n: int) -> int:
    res = ""
    for i in range(1, n+1):
        res += str(i)
    return len(res)

print(page_digits(4))
print(page_digits(1000000)) #Print: 5888896

'''
[1-9] -> 9 
    123456789

[10-99] -> 180

[100-999] -> 2 700

[1000-9999] -> 36 000

[10000-99999] -> 450 000
'''

