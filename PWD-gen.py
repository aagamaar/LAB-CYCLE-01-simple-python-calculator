import random
import string

def generate_password(length):
    """Generates a random password of the specified length.

    Args:
        length: The desired length of the password.

    Returns:
        A randomly generated password.
    """

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated password:", password)