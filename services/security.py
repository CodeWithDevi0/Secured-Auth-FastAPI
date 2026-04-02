import bcrypt
import os

PEPPER = "IMissYouBoss4574"

def generate_salt() -> str:
   # generates a random 16-byte salt as a hex string
   return os.urandom(16).hex()

def hash_password(password: str, salt: str) -> str:
   # combines password, salt, and pepper, then hashes with bcrypt
   combined_string = password + salt + PEPPER
   hashed_password = bcrypt.hashpw(combined_string.encode("UTF-8"), bcrypt.gensalt())
   return hashed_password

def verify_password(plain_password: str, db_salt: str, db_hashed: str) -> bool:
   # recreates the combined string and verifies it against the stored hash
   combined_string = plain_password + db_salt + db_hashed
   return bcrypt.checkpw(combined_string.encode("UTF-8"), db_hashed.encode("UTF-8"))

