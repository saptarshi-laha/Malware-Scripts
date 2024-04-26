#Author - ExploitedSite

import base64

def main():
    encrypted_configuration = "config_here"

    # Decode the full base64 data
    full_decoded_data = base64.b64decode(encrypted_configuration)

    # Extract XOR key (first 32 bytes)
    xor_key = full_decoded_data[:32]
    encrypted_data = full_decoded_data[32:]

    # XOR decryption
    decrypted_data = bytes([encrypted_data[i] ^ xor_key[i % len(xor_key)] for i in range(len(encrypted_data))])

    # Print the decrypted data as a string
    print(decrypted_data.decode('utf-8', errors='ignore'))

if __name__ == "__main__":
    main()
