def encrypt_text(input_text, shift, output_file):
    encrypted_text = ""
    for char in input_text:
        if char.isalpha():  # Encrypt only alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged

    with open(output_file, 'w') as file:
        file.write(encrypted_text)

    return encrypted_text


# Example Usage
plaintext = input("Enter the text to encrypt: ")
shift_value = int(input("Enter the shift value: "))
encrypt_text(plaintext, shift_value, "encrypted.txt")
print(f"Encrypted text saved to 'encrypted.txt'.")
