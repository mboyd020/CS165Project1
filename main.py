import hashlib
from multiprocessing import Pool, cpu_count

fullHash = "team5:$1$zLGo2l86$srZPtyJQb2sQIaMdtHosV1:16653:0:99999:7:::"
salt = b"zLGo2l86"
hash = b"srZPtyJQb2sQIaMdtHosV1"
correct_guess_lts = open("correct.txt", "w")
def guess(guess):
  hashed = hashlib.md5(guess + salt)
  if (hashed.hexdigest() == hash):
    print(guess)
    correct_guess_lts.write(guess)
    exit()
  return False

pool = Pool(cpu_count())
# pool.map(guess, [b"123456", b"password", b"123456789", b"12345678", b"12345", b"1234567", b"qwerty", b"abc123", b"monkey", b"letmein", b"111111", b"123123", b"admin", b"welcome", b"1234567890"])

total_passwords = 321272406

while True:
    i = 0
    passwords_current_array = []
    passwords_file = open("passwords.txt", "r")
    
    for line in passwords_file:
        if i >= 100000:
            break
      i += 1
      passwords_current_array.append(line.strip().encode())
    print(passwords_current_array[i-1])
    pool.map(guess, passwords_current_array)
