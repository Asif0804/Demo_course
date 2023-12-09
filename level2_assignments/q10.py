def stone(n):
    if n % 2 == 0:
      s = list(range(2, n + 1, 2))
    else:
        s = list(range(2, n, 2))
    return s

n = int(input("Enter the stones piles:"))
stone(n)