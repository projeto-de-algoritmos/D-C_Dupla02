def calcPower(left, right, B, totalAvengers):
    return B * totalAvengers * (right - left + 1)

def upperBound(x, avengers):
    lo, up = 0, len(avengers)
    while lo < up:
        mid = (lo + up)//2
        if x < avengers[mid]:
            up = mid
        else:
            lo = mid + 1
    return lo

def lowerBound(x, avengers):
    lo, up = 0, len(avengers)
    while lo < up:
        mid = (lo + up)//2
        if x <= avengers[mid]:
            up = mid
        else:
            lo = mid + 1
    return lo


def checkTotalAvengers(avengers, left, right):
    totalAvengers = upperBound(right, avengers) - lowerBound(left,avengers)

    return totalAvengers

def findMinimumPower(left, right, A, B, avengers):
    totalAvengers = checkTotalAvengers(avengers, left, right)
    if totalAvengers == 0:
        return A

    if left == right:
        return calcPower(left, right, B, totalAvengers)

    middle = left + int((right - left) / 2)

    minLeft = findMinimumPower(left, middle, A, B, avengers)
    minRight = findMinimumPower(middle + 1, right, A, B, avengers)

    return min((minLeft + minRight), calcPower(left, right,B,totalAvengers))


if __name__ == '__main__':
    n, k, A, B = map(int, input().split())

    baseLength = pow(2, n)

    avengers = sorted(list(map(int, input().split())))

    print(findMinimumPower(1, baseLength, A, B, avengers))
