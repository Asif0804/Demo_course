def encoding(input_str):
    updated_str = ""
    count = 1
    a=len(input_str)
    for i in range(1,a,1):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            updated_str += input_str[i - 1] + str(count)
            count = 1

    updated_str += input_str[-1] + str(count)

    return updated_str

input_string = "wwwwaaadebbbbbw"
print(encoding(input_string))