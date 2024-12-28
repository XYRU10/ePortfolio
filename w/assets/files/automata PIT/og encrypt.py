# Encryption Script

# Helper Functions
def caesar_encrypt(text, shift):
    """Encrypts text using Caesar cipher."""
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    """Decrypts text using Caesar cipher."""
    return caesar_encrypt(text, -shift)

def transposition_encrypt(text):
    """Encrypts text using a simple transposition cipher."""
    return text[::-1]  # Reverse the text

def transposition_decrypt(text):
    """Decrypts text using a simple transposition cipher."""
    return text[::-1]  # Reverse the text

def replace_vowels_encrypt(text):
    """Replaces vowels with assigned numbers and applies another Caesar cipher."""
    vowel_map = {'a': '0', 'e': '1', 'i': '2', 'o': '3', 'u': '4',
                 'A': '0', 'E': '1', 'I': '2', 'O': '3', 'U': '4'}
    encrypted = ""
    for char in text:
        if char.lower() in vowel_map:
            encrypted += vowel_map[char.lower()]
        else:
            encrypted += char
    return caesar_encrypt(encrypted, 2)  # Apply a Caesar shift of 2

def replace_vowels_decrypt(text):
    """Decrypts text by reversing the vowel replacement and Caesar cipher."""
    text = caesar_decrypt(text, 2)
    vowel_map = {'0': 'a', '1': 'e', '2': 'i', '3': 'o', '4': 'u'}
    decrypted = ""
    for char in text:
        if char in vowel_map:
            decrypted += vowel_map[char]
        else:
            decrypted += char
    return decrypted

def triple_encrypt(plaintext, caesar_shift=3):
    """Applies three layers of encryption."""
    # First Layer: Caesar Cipher
    layer1 = caesar_encrypt(plaintext, caesar_shift)
    # Second Layer: Transposition Cipher
    layer2 = transposition_encrypt(layer1)
    # Third Layer: Replace Vowels + Caesar Cipher
    layer3 = replace_vowels_encrypt(layer2)
    return layer3

def triple_decrypt(ciphertext, caesar_shift=3):
    """Applies three layers of decryption."""
    # Third Layer: Replace Vowels + Caesar Cipher
    layer2 = replace_vowels_decrypt(ciphertext)
    # Second Layer: Transposition Cipher
    layer1 = transposition_decrypt(layer2)
    # First Layer: Caesar Cipher
    plaintext = caesar_decrypt(layer1, caesar_shift)
    return plaintext

def analyze_state_transitions(plaintext, caesar_shift=3):
    print("\nComposite Automata State Transition Analysis:")

    # Layer 1: Caesar Cipher
    layer1 = caesar_encrypt(plaintext, caesar_shift)
    print("\nLayer 1 (Caesar Cipher):")
    for i, (char, encrypted_char) in enumerate(zip(plaintext, layer1)):
        print(f"State {i}: '{char}' -> '{encrypted_char}'")

    # Layer 2: Transposition Cipher
    layer2 = transposition_encrypt(layer1)
    print("\nLayer 2 (Transposition Cipher):")
    print(f"Input: '{layer1}'")
    print(f"Output: '{layer2}'")

    # Layer 3: Replace Vowels + Caesar Cipher
    layer3 = replace_vowels_encrypt(layer2)
    print("\nLayer 3 (Replace Vowels + Caesar Cipher):")
    for i, (char, encrypted_char) in enumerate(zip(layer2, layer3)):
        print(f"State {i}: '{char}' -> '{encrypted_char}'")

    print("\nFinal Encrypted Text:", layer3)
# Main Function
if __name__ == "__main__":
    print("Enhanced Encryption Tool")

    while True:
        print("\nOptions:")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Analyze State Transitions")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            plaintext = input("Enter the plaintext: ")
            encrypted_text = triple_encrypt(plaintext)
            print(f"Encrypted Text: {encrypted_text}")

        elif choice == "2":
            ciphertext = input("Enter the ciphertext: ")
            decrypted_text = triple_decrypt(ciphertext)
            print(f"Decrypted Text: {decrypted_text}")

        elif choice == "3":
            plaintext = input("Enter the original text: ")
            analyze_state_transitions(plaintext)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")
