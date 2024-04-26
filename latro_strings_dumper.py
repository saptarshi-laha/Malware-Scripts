def decrypt_byte_string(byte_string):
    decrypted_string = b''
    for i, byte in enumerate(byte_string):
        decrypted_byte = byte ^ (0x7f + i) % 256
        decrypted_string += bytes([decrypted_byte])
    try:
        decoded_string = decrypted_string.decode('utf-8', errors='ignore')
    except UnicodeDecodeError:
        decoded_string = decrypted_string.decode('utf-16', errors='ignore').encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
    return decoded_string.replace('\x00', '')


def main():
    offset = 0xCE00
    length = 0x1600

    with open('latro_dumped.bin', 'rb') as f:
        f.seek(offset)
        binary_data = f.read(length)

    byte_strings = []
    current_byte_string = b''
    recording = False

    for byte in binary_data:
        if byte == 0xD0:
            recording = True
            current_byte_string = b''
        elif byte == 0x00 and recording:
            recording = False
            if current_byte_string:
                byte_strings.append(current_byte_string)
        elif recording:
            current_byte_string += bytes([byte])

    with open('decrypted_strings.txt', 'w', encoding='utf-8', errors='ignore') as f:
        for byte_string in byte_strings:
            decrypted_string = decrypt_byte_string(byte_string)
            f.write(decrypted_string + '\n')


if __name__ == "__main__":
    main()
