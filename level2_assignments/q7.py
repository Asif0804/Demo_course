def median(num):
    a = sorted(num)
    n = len(a)

    if n % 2 == 1:
        return a[n // 2]
    else:
        mid1 = a[(n // 2) - 1]
        mid2 = a[n // 2]
        return (mid1 + mid2) / 2

num = [7,2,5,1,9,3]
median(num)