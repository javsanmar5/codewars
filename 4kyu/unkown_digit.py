def solve_runes(runes: str) -> int:

    OPERATORS = ['+', '*', '=']

    acc = 0
    num1 = ""
    num2 = ""
    res = ""

    #We parse the runes
    for i in runes:
        if acc == 0:
            if i in OPERATORS or (i == "-" and num1 != ""):
                op = i
                acc += 1
            else:
                num1 += i

        elif acc == 1:
            if i not in OPERATORS:
                num2 += i
            else:
                acc += 1
        else:
            res += i


    for i in range(0,10):
        num1a = num1.replace('?', str(i))
        num2a = num2.replace('?', str(i))
        resa = res.replace('?', str(i))

        if ('?' in num1 and i == 0 and num1.index('?') == 0 and len(num1) > 1) or ('?' in num2 and i == 0 and num2.index('?') == 0 and len(num2) > 1) or ('?' in res and i == 0 and res.index('?') == 0 and len(res) > 1) or (str(i) in num1 or str(i) in num2 or (str(i) in res)):
            continue
        if (num1[0] == '-' and '?' in num1 and i == 0 and num1.index('?') == 1 and len(num1) > 2) and (num2[0] == '-' and '?' in num2 and i == 0 and num2.index('?') == 1 and len(num2) > 2) or (res[0] == '-' and '?' in res and i == 0 and res.index('?') == 1 and len(res) > 2):
            continue

        match op:
            case '*':
                if int(num1a) * int(num2a) == int(resa):
                    return i
            case '+':
                if int(num1a) + int(num2a) == int(resa):
                    return i
            case '-':
                if int(num1a) - int(num2a) == int(resa):
                    return i
                
    return -1




    




#[number][op][number]=[number]
runes = "?*11=??"
print(solve_runes(runes))

