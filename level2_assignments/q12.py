def login_page():
    username = input("Enter your username: ")

    password = input("Enter your password: ")

    for attempt in range(3):
        confirm_password = input("Re-enter your password to confirm: ")

        if password == confirm_password:
            print("Login successful")
            break
        else:
          print("Password mismatch, Please check the Password")
    else:
      print("You Reached maximum number of attempts. Login failed.")


login_page()