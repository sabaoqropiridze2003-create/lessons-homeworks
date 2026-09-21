from pwdlib import PasswordHash

password_hasher = PasswordHash.recommended()
def hash_password(password :str):
    return password_hasher.hash(password)

def verify_password(password: str, hashed_password: str):
    return password_hasher.verify(password, hashed_password)


# hashed_password = hash_password("saba")
# print(verify_password("saba", hashed_password))