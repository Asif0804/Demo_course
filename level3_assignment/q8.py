def parse(encoded_str,numberof_parts):
    parts = encoded_str.split("0")
    parts = [part for part in parts if part]

    if len(parts) == numberof_parts:
        result_dict = {
            "first_name": parts[0],
            "last_name": parts[1],
             "id": parts[2]
        }
        return result_dict
    else:
        return None


encoded_string = "asif0mus023"
number_parts=3
print(parse(encoded_string,number_parts))