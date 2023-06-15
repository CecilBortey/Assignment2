name = "roddy ricch"
code = "12345"

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == name and password == code:
    print("Login Successful")
elif username != name and password != code:
    print("Wrong input, you have 2 more attempts!!")
    count = 0
    while count < 2:
        username = input("Re-enter your username: ")
        password = input("Re-enter your password: ")
        count += 1
        if username == name and password == code:
            print("Login Successful")
            break
        if count == 2:
            print("Wrong credentials.... try again after 5 minutes. ")      