email = input("Enter your Email: ")  # e.g., g@g.in, lscube@gmail.com
k, j, d = 0, 0, 0
if len(email) >= 6:  # 1
    if email[0].isalpha():  # 2
        if ("@" in email) and (email.count("@") == 1):  # 3
            if (email[-4] == ".") ^ (email[-3] == "."):  # 4
                for i in email:
                    if i.isspace():  # 5
                        k = 1
                    elif i.isalpha():
                        if i.isupper():  # 5
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in "_.@":
                        continue
                    else:  # 5
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 2")
        else:
            print("Wrong Email 1")
    else:
        print("Wrong Email - must start with letter")
else:
    print("Wrong Email - too short")