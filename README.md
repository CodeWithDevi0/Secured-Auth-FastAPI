# Secured Authentication API

*A modular FastAPI and MySQL backend I built to learn professional security practices, cryptography, and secure user authentication.*

## What I Learned in this Project
Instead of putting all my code in one massive file, I learned how to organize a project professionally by separating the logic:

- **Advanced Project Organization:** I reinforced my understanding of separating logic (Routers, Services, Database) and added a dedicated `security.py` service to isolate my cryptography logic from the rest of the application.
- **Cryptography & Bcrypt:** I learned why plain text passwords are dangerous and how to use the industry-standard `bcrypt` library to apply slow-hashing algorithms that prevent brute-force attacks.
- **Salting & Peppering:** I learned how to use Python's `os.urandom` to generate a unique 16-byte hex "salt" for every user to defeat dictionary attacks. I also learned how to implement a hidden constant "pepper" for an extra layer of backend security, while navigating bcrypt's strict 72-byte limit.
- **Role-Based Access Control (RBAC):** I learned how to design a relational database with a `roles` table (Admin, Educator, User) and how to enforce a default role (`DEFAULT 3`) directly at the database level instead of relying on the API logic.
- **Database Result Mapping:** I learned how to handle raw data returned from MySQL as Tuples. I practiced accessing specific database fields using Python's integer indexing (e.g., `row[0]`) to retrieve usernames, salts, and hashes during the authentication process.
- **Git & Environment Management:** I learned how to use a `.gitignore` file to keep my repository clean by ignoring the massive `venv/` folder, and how to use `pip freeze > requirements.txt` so other developers can easily install my project's dependencies.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Security:** Bcrypt (Cryptography)
- **Database:** MySQL (XAMPP)
- **CORS:** Pre-configured so my future Vue.js frontend can easily connect to it.

## Current Features
- `POST /api/auth/register` — Securely registers a new user with a uniquely salted and peppered password hash, automatically assigning them a default standard user role.
- `POST /api/auth/login` — Authenticates a user by retrieving their unique salt from the database and verifying their credentials against the stored hash.

## WIP
- `Not finish yet` - This repository is solely my practice area