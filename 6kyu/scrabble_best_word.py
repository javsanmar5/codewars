def get_best_word(points: tuple, words: list) -> int:
    ABC = 'abcdefghijklmnopqrstuvwxyz'
    dicc = {}
    for i in words:
        value = 0
        for j in i:
            value += points[ABC.index(j.lower())]
        if i not in dicc:
            dicc[i] = value
    
    res = (0,0,0)
    cont = 0
     
    for k, v in dicc.items():
        if v > res[0]:
            res = (v, len(k), cont)
        elif v == res[0] and len(k) < res[1]:
            res = (v, len(k), cont)
        
        cont += 1

    return res[2]
        





list1, list2 = (1,3,3,2,1,4,2,4,1,8,10,1,2,1,1,3,8,1,1,1,1,4,10,10,10,10), ["AABCDEF", "WHO","IS","THE","BEST","OF","US"]
print(get_best_word(list1,list2))


