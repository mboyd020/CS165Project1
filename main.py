import crypt
import time
# from multiprocessing import Pool, cpu_count

fullHash = "team5:$1$zLGo2l86$srZPtyJQb2sQIaMdtHosV1:16653:0:99999:7:::"
salt = "$1$zLGo2l86"  # Include the "$1$" prefix for MD5 in crypt
hash = "srZPtyJQb2sQIaMdtHosV1"
correct_guess_lts = open("correct.txt", "w")

def guess(guess):
    # print("Guessing " + guess.decode() + salt)
    hashed = crypt.crypt(guess.decode(), salt)
    if hashed.split('$')[-1] == hash:
        print(guess.decode())
        correct_guess_lts.write(guess.decode() + "\n")
        exit()
    return False

# pool = Pool(cpu_count())

total_passwords = 0
complexity = 6
for i in range (1,complexity + 1):
    total_passwords += 26 ** i

starting_password = total_passwords - 26 ** complexity

i = starting_password
passwords_file = open("passwords.txt", "r")
startTime = time.time()
passwords_file.seek(starting_password)
for line in passwords_file:
    guess(line.strip().encode())
    if (i % 100000 == 0) and i != 0:
        print(f"Checking password: {line}, {i} of {total_passwords - 1}...")
        elapsed = time.time() - startTime
        print(f"Time Elapsed: {elapsed} seconds")
        print(f"Currently running @ {i/elapsed} hashes per second")
    i += 1
