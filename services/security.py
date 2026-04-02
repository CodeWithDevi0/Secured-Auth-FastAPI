import bcrypt
import os

PEPPER = "IMissYouBoss4574"

def generate_salt() -> str:
   # generates a random 16-byte salt as a hex string
   return os.urandom(16).hex()

def hash_password(password: str, salt: str) -> str:
   # combines password, salt, and pepper, then hashes with bcrypt
    combined_string = password + salt + PEPPER
    
    # Bcrypt has a 72-byte limit, so we 'slice' just in case [cite: 110]
    prepared_password = combined_string.encode('utf-8')[:72]
    
    # gensalt() handles the internal work, but we store our manual salt separately [cite: 40]
    hashed_password = bcrypt.hashpw(prepared_password, bcrypt.gensalt())
    
    # Return as a string for database storage
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, db_salt: str, db_hashed: str) -> bool:
   # recreates the combined string and verifies it against the stored hash
   combined_string = plain_password + db_salt + PEPPER
   
   prepared_password = combined_string.encode('utf-8')[:72]
   
   # bcrypt.checkpw automatically compares the new attempt with the stored hash [cite: 52]
   return bcrypt.checkpw(prepared_password, db_hashed.encode('utf-8'))

