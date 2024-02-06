def main(arr: list) -> int:
    posiciones = primer_numbers_under(len(arr))
    acum = 0
    for i in posiciones:
        acum += arr[i]

    return posiciones

def primer_numbers_under(n):
    return [i for i in range(2, n) if is_prime(i)]
    

def is_prime(n):
    if n == 4: return False
    for i in range(2, n//2):
        if n % i == 0:
            return False

    return True

    
if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    #print(main(arr))
    
    print(is_prime(4))
