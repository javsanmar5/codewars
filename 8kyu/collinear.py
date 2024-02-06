

def main(x1, y1, x2, y2):
    if (x1, y1) == (0,0) or (x2, y2) == (0,0): return True  

    if x1 != 0 and x2 != 0:
        return y1 / x1 == y2 / x2
    else:
        return x1 == 0 and x2 == 0
    

def one_line(x1, y1, x2, y2):
    return True if (x1, y1) == (0,0) or (x2, y2) == (0,0) else y1 / x1 == y2 / x2 if x1 != 0 and x2 != 0 else x1 == 0 and x2 == 0
    
if __name__ == '__main__':
    print(main(1,2,2,4))
    print(one_line(1,2,2,4))