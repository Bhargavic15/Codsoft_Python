import random
import string

def generate_password(length=12):
    """
    Generate a random password.

    :param length: Length of the password
    :return: A random password string
    """
    if length < 4:  # Ensure the length is at least 4 for a mix of character types
        raise ValueError("Password length should be at least 4 characters.")
    
    # Define possible characters for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length-4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        password = generate_password(length)
        print(f"Generated password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
