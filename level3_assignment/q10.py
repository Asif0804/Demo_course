def assign_computers_cafe(N, customers):
    computers_status = [False] * N

    for customer in customers:
        if any(computer == False for computer in computers_status):

            for i in range(N):
                if not computers_status[i]:
                    computers_status[i] = True
                    print(f"Customer {customer} is using Computer {i + 1}.")
                    break
        else:
            print("No avalible Computers")

N = 4
customer_arrivals = [1, 2, 3, 4, 5, 6]
assign_computers_cafe(N, customer_arrivals)