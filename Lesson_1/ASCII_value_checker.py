print("ASCII Value Checker")
print("========================================")

char = input("Enter a single character: ")

if len(char) == 1:
    ascii_val = ord(char)

    print(f"\nCharacter: '{char}'")
    print(f"ASCII Value: {ascii_val}")

    print("\nCharacter Type: ", end="")

    if char.isupper():
        print("Uppercase Letter")
    elif char.islower():
        print("Lowercase Letter")
    elif char.isdigit():
        print("Digit")
    elif char == " ":
        print("Space")
    else:
        print("Special Character")

else:
    print("\n\033[31mError\033[0m: Please enter exactly ONE character!\n")