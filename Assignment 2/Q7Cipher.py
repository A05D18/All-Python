# Cipher dictionary (plaintext to ciphertext)
cipher = {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j',
          'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q',
          'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x',
          'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}

# Create reverse mapping for decryption (ciphertext to plaintext)
reverse_cipher = {v: k for k, v in cipher.items()}

# Encrypted string
encrypted = 'sbwkrq'

# Decrypt the string
decrypted = ''
for char in encrypted:
    decrypted += reverse_cipher[char]

print("Decrypted:", decrypted)