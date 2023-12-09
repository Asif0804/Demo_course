def leve2_4(array_size, D):
    N = len(array_size)
    rotated_arr = array_size[N - D:] + array_size[:N - D]
    return rotated_arr

rotated_array = leve2_4([1, 2, 3, 4, 5], D=2)