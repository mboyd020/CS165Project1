#create a file that contains all lowercase passwords from a-z of length 6 or less
password_file = open("passwords.txt", "w")
count = 0
for i in range(1, 7):
    print("Generating passwords of length " + str(i) + "...")
    for j in range(0, 26**i):
        password = ""
        num = j
        for k in range(i):
            password += chr(num % 26 + 97)
            num //= 26
        password_file.write(password + "\n")
        count += 1
        if (count % 1000000) == 0:
            print(f"{(count/321272406) * 100}% done")
print("done")
password_file.close()