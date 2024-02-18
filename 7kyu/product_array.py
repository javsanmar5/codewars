def product_array(numbers: list) -> list:
    res = list()
    for i in range(len(numbers)):
        aux = []
        if i != len(numbers) -1:
            aux.append(numbers[i+1:])
        if i != 0:
            aux.append(numbers[:i])
        res.append(aux)





print(product_array([1,2,3,4,5]))
        