import hashlib
fullHash = "team5:$1$zLGo2l86$srZPtyJQb2sQIaMdtHosV1:16653:0:99999:7:::"
salt = "zLGo2l86"
hash = "srZPtyJQb2sQIaMdtHosV1"
def guess(guess):
  if (hashlib.md5(guess + salt).hexdigest() == testhash):
    print(guess)
    return true
  return false
testhash = hashlib.md5("abc" + salt).hexdigest()
guess("abc")
