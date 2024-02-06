def simplify(poly:str) -> str:

    dic = dict()
    lista = []
    word = ""
    res = list()

    for i in range(len(poly)):
        if i == 0 and poly[i] != '-' and poly[i] != '+': word += "+" 
        if (poly[i] == "+" or poly[i] == "-") and word != "":
            lista.append(word)
            word = ""
        word += poly[i]
        if i == len(poly) - 1:
            lista.append(word)
        

    aux = ["".join(sorted(i)) for i in lista]
    for i in range(len(aux)):
        if not aux[i][1].isdigit():
            aux[i] = aux[i][:1] + '1' + aux[i][1:]


    for i in aux:
        number = 0
        string = ""
        if i[0] == "+":
            for j in i:
                if j.isdigit(): number += int(j)
                elif j != "+": string += j
        if i[0] == "-":
            for j in i:
                if j.isdigit(): number -= int(j)
                elif j != "-": string += j
        if string in dic:
            dic[string] += number
        else:
            dic[string] = number


    for k, v in dic.items():
        word = ""
        if v > 0:
            sign = "+"
        elif v < 0:
            sign = "-"

        if v != 0: 
            if abs(v) != 1:
                word = sign + str(abs(v)) + k
            else:
                word = sign + k
            
        if word != "": res.append(word)          


    res = custom_sort(res)

    res = "".join(res)

    if res[0] == "+":
        return res[1:]
    else: 
        return res


def custom_sort(lst):
    def custom_key(string):
        not_char = '+-1234567890'
        actual_string = ""
        for char in string:
            if char not in not_char:
                actual_string += char
        return len(actual_string), actual_string

    return sorted(lst, key=custom_key)




poly = "+n-5hn+7tjhn-4nh-3n-6hnjt+2jhn+9hn"

print(simplify(poly))

