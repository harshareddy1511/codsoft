import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    
    # Get the desired password length from the user
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    # Ask user for password complexity options
    print("\nSelect the password complexity:")
    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Define the character pool based on user choices
    character_pool = string.ascii_lowercase  # Lowercase letters are mandatory
    if include_upper:
        character_pool += string.ascii_uppercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    # Ensure the character pool is not empty
    if not character_pool:
        print("You must select at least one character type for the password.")
        return

    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    generate_password()
