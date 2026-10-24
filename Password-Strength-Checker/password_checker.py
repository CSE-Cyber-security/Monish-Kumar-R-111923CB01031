
import string
import getpass


def check_password_strength(password):
    # Check the five password criteria
    length_ok = len(password) >= 8
    uppercase_ok = any(char in string.ascii_uppercase for char in password)
    lowercase_ok = any(char in string.ascii_lowercase for char in password)
    number_ok = any(char in string.digits for char in password)
    symbol_ok = any(
        char in string.punctuation for char in password
    )

    # Display the results
    print("\n--- Password Strength Report ---")
    print("Length:", "Satisfied" if length_ok else "Not Satisfied")
    print("Uppercase:", "Satisfied" if uppercase_ok else "Not Satisfied")
    print("Lowercase:", "Satisfied" if lowercase_ok else "Not Satisfied")
    print("Numbers:", "Satisfied" if number_ok else "Not Satisfied")
    print("Symbols:", "Satisfied" if symbol_ok else "Not Satisfied")

    # Calculate password strength
    score = sum([
        length_ok,
        uppercase_ok,
        lowercase_ok,
        number_ok,
        symbol_ok
    ])

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print("Password Strength:", strength)


def main():
    password = getpass.getpass("Enter your password: ")
    check_password_strength(password)


if __name__ == "__main__":
    main()
