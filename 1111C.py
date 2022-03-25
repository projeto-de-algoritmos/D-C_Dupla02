def calcPower(positions, A, B):
    totalAvengers = 0

    for i in positions:
        totalAvengers = totalAvengers + i

    if totalAvengers == 0:
        return A
    else:
        return B * totalAvengers * len(positions)


def findMinimumPower(positions, A, B):
    if len(positions) == 1:
        return calcPower(positions, A, B)

    middle = int(len(positions) / 2)

    L = positions[:middle]
    R = positions[middle:]

    minLeft = findMinimumPower(L, A, B)
    minRight = findMinimumPower(R, A, B)

    return min((minLeft + minRight), calcPower(positions,A,B))

if __name__ == '__main__':
    n, k, A, B = map(int, input().split())

    positions = [0] * pow(2, n)

    avengers = list(map(int, input().split()))

    for i in avengers:
        positions[i - 1] = positions[i - 1] + 1

    print(findMinimumPower(positions,A,B))

