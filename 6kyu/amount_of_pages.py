def amount_of_pages(summary: int) -> int:
    res = ""
    for i in range(1, summary+1):
        res += str(i)
        if len(res) == summary:
            return i
    return -1


