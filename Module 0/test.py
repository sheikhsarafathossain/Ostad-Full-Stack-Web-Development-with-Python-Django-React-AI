import hashlib
import os

def hash_password(password: str) -> str:
    salt = os.urandom(16)  # 16 bytes random salt
    pwd_hash = hashlib.pbkdf2_hmac(
        'sha256',                 # Hash algorithm
        password.encode(),        # Password
        salt,                     # Salt
        100_000                   # Iterations (important!)
    )
    return salt.hex() + ":" + pwd_hash.hex()

def verify_password(stored_password: str, provided_password: str) -> bool:
    salt_hex, hash_hex = stored_password.split(":")
    salt = bytes.fromhex(salt_hex)

    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode(),
        salt,
        100_000
    )
    print(new_hash.hex())
    print(hash_hex)
    return new_hash.hex() == hash_hex

# 7592e6bd0608663b43c8d1359b3f702e6edcc3cc479181ee8b0b12ffae5f2a6e
# Register
stored = hash_password("MyStrongPassword123")

# Login
is_valid = verify_password(stored, "MyStrongPassword123")
print(is_valid)  # True
