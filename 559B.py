
def divideOrdena(string):
    if len(string) % 2:
        return string

    a = divideOrdena(string[:len(string)//2])
    b = divideOrdena(string[len(string)//2:])

    if (a < b):
        return a + b
    else:
        return b + a

if __name__ == '__main__':
    a = input()
    b = input()

    if divideOrdena(a) == divideOrdena(b):
        print('YES')
    else:
        print('NO')