def decrypt_text(input_file, shift):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()

    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Decrypt only alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged

    return decrypted_text


# Example Usage
shift_value = int(input("Enter the shift value used for encryption: "))
decrypted_text = decrypt_text("encrypted.txt", shift_value)
print(f"Decrypted text: {decrypted_text}")
