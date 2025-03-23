#TASK 3
import random
import string

def get_password_length():
    """Prompt the user to specify the desired length of the password."""
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                return length
            else:
                print("Password length must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_password(length):
    """Generate a random password of the specified length."""
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)


print("Welcome to the CodSoft Password Generator!")
print("This tool will help you create a strong and random password.")

# Get the desired password length from the user
length = get_password_length()
# Generate the password
password = generate_password(length)
# Display the generated password
print(f"\nYour CodSoft generated password is: {password}")
print("Make sure to store it securely!")

