from database.connection import get_db_connection
from services import security

def execute_read_query(sql: str, values: tuple = None, fetch_one: bool = False):
   conn = get_db_connection()
   if not conn:
      return {"error": "Database connection Failed"}
   
   cursor = conn.cursor()

   if values:
      cursor.execute(sql, values)
   else:
      cursor.execute(sql)

   if fetch_one:
      result = cursor.fetchone()
   else:
      result = cursor.fetchall()

   cursor.close()
   conn.close()
   return result


def execute_write_query(sql: str, values: tuple = None):
   conn = get_db_connection()
   if not conn:
      return 0, 0
   
   cursor = conn.cursor() # No dictionary needed

   if values:
      cursor.execute(sql, values)
   else:
      cursor.execute(sql)

   conn.commit() # save the changes
   rows_affected = cursor.rowcount
   last_insert_id = cursor.lastrowid

   cursor.close()
   conn.close()
   return rows_affected, last_insert_id



def register_user_in_db(user_data):
   try:
      # Check if the username already exist
      check_sql = "SELECT * FROM users WHERE username = %s"
      existing_user = execute_read_query(check_sql, (user_data.username,), fetch_one=True)

      # if it reutrns a dictionary instead of None, the user exist
      if existing_user and not isinstance(existing_user, dict) and "error" in existing_user:
         return existing_user
      if existing_user:
         # returns db connection error 
         return{"error": "Username Already Exists"}
      
      # Bcrypt
      salt = security.generate_salt()
      hashed_password = security.hash_password(user_data.password, salt)

      # inserting to database
      insert_sql = "INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)"
      values = (
         user_data.username,
         hashed_password,
         salt
      )

      rows_affected, _, = execute_write_query(insert_sql, values)

      if rows_affected > 0:
         return {"message": "User registered successfully!"}
      else:
         return {"error": "Failed to register user."}
   except Exception as e:
      print(f"Internal Database Error: {e}")
      return{"error": "Oops! something went wrong on our end. Please try again later!"}
   


def login_user_in_db(user_data):
    try:
        # fetch the user's secure data
        sql = "SELECT password_hash, salt FROM users WHERE username = %s"
        db_user = execute_read_query(sql, (user_data.username,), fetch_one=True)

        if not db_user or ("error" in db_user if isinstance(db_user, dict) else False):
            # Rubric constraint: Exact phrasing required
            return {"error": "Invalid Username or Password"}

        # vverify the password against the database hash
        is_valid = security.verify_password(user_data.password, db_user['salt'], db_user['password_hash'])

        if is_valid:
            return {"message": "Login Successful"}
        else:
            return {"error": "Invalid Username or Password"}
            
    except Exception as e:
        print(f"Internal Database Error: {e}")
        return {"error": "Oops! Something went wrong on our end while logging in."}