
 Password Strength Checker

## About the Project
The Password Strength Checker is a simple Python application
that evaluates password strength using five basic security
criteria. It helps users understand password security and
demonstrates Python concepts such as strings, loops,
conditional statements, and functions.

 Objectives
- Check password length.
- Identify uppercase and lowercase letters.
- Check for numeric digits.
- Identify special characters.
- Classify passwords as Weak, Medium, or Strong.

 Requirements
- Python 3.x
- Any Python editor or terminal

 Password Criteria
1. Length: At least 8 characters.
2. Uppercase: At least one uppercase letter (A-Z).
3. Lowercase: At least one lowercase letter (a-z).
4. Numbers: At least one digit (0-9).
5. Symbols: At least one special character.

 How to Run
1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

   python password_checker.py

5. Enter a password when prompted.

 Example
Input:
Hello@123

Expected output:
--- Password Strength Report ---
Length: Satisfied
Uppercase: Satisfied
Lowercase: Satisfied
Numbers: Satisfied
Symbols: Satisfied
Password Strength: Strong

 Strength Classification
- Strong: All five criteria are satisfied.
- Medium: Three or four criteria are satisfied.
- Weak: Zero, one, or two criteria are satisfied.

 Project Structure
Password-Strength-Checker/
├── password_checker.py
├── README.md
└── screenshots/
    └── output.png

 Concepts Used
- Python strings
- Conditional statements
- Functions
- The any() function
- The string and getpass modules

 Disclaimer
This is an educational password checker. It evaluates
basic password composition and does not guarantee that
a password is secure against modern attacks.

 Author
Monish kumar R