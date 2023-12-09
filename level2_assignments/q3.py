
def count(array, k):
    a = 0
    b = set()

    for num in array:
        c = k - num
        if c in b:
            a += 1
        b.add(num)

    return a
array = [1,2,3,4,5,6]
k = 6
count(array,k)