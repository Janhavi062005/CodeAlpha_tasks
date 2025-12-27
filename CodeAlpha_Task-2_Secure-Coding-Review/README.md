# Task 2: Secure Coding Review

## Objective
The objective of this task is to analyze an existing program from a security perspective, identify vulnerabilities in the code, understand their potential impact, and apply secure coding practices to mitigate those risks.

---

## Description
In this task, I performed a **secure code review** on a simple Python-based login system.  
The task involved reviewing an intentionally insecure version of the program, identifying security flaws, and then implementing a more secure version by following basic security best practices.

Two versions of the program are included:
- `vulnerable_code.py` – contains intentional security weaknesses
- `secure_code.py` – improved version with security fixes applied

---

## Files Included
- `vulnerable_code.py` – Demonstrates common security mistakes
- `secure_code.py` – Secured version of the same program
- `README.md` – Explanation of vulnerabilities and fixes

---

## Vulnerability Analysis (Insecure Version)

### 1. Hardcoded Credentials
The username and password were directly written in the source code.

**Risk:**
- Anyone with access to the code can see the credentials.
- Credentials cannot be changed without modifying the code.

---

### 2. Plain-Text Password Handling
Passwords were taken and compared in plain text.

**Risk:**
- Passwords can be exposed through memory dumps or logs.
- Increases the risk of credential theft.

---

### 3. No Password Hashing
The program compared passwords directly instead of using cryptographic hashing.

**Risk:**
- Violates basic password security standards.
- Plain-text passwords are vulnerable if data is leaked.

---

### 4. No Input Validation
User input was accepted without any validation.

**Risk:**
- Opens the possibility of injection-style attacks in larger applications.
- Can lead to unexpected behavior.

---

### 5. No Protection Against Brute-Force Attempts
The program allowed unlimited login attempts.

**Risk:**
- Enables brute-force and credential-guessing attacks.

---

## Secure Code Improvements

The following security improvements were implemented in `secure_code.py`:

### 1. Password Hashing
- Passwords are hashed using SHA-256 before comparison.
- Only hashed passwords are stored and compared.

---

### 2. Hidden Password Input
- The `getpass` module is used to hide password input.
- Prevents passwords from being displayed on the screen.

---

### 3. Separation of Authentication Logic
- Authentication logic is moved into a separate function.
- Improves readability, maintainability, and security.

---

### 4. Reduced Exposure of Sensitive Data
- No credentials are printed or logged.
- Sensitive operations are handled securely.

---

## Tools and Technologies Used
- Python 3
- `hashlib` for password hashing
- `getpass` for secure password input

---

## How to Run the Programs

### Run the Insecure Version
```bash
python vulnerable_code.py
```
Run the Secure Version
```bash
python secure_code.py
```


###Try logging in with:

Username: admin

Password: admin123

##Observations

- Hardcoded credentials are one of the most common real-world security issues.

- Password hashing significantly improves security with minimal code changes.

- Secure coding practices can greatly reduce risks even in small programs.
  
---

##Learning Outcome

**Through this task, I learned:**

- How to identify common security vulnerabilities in code

- Why hardcoded credentials and plain-text passwords are dangerous

- How password hashing improves authentication security

- The importance of separating logic for better security and maintainability

- How to approach code review from a security perspective

---

