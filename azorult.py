import re

def xor_bytes(bytes1, bytes2):
    return bytes(a ^ b for a, b in zip(bytes1, bytes2))

def find_http_strings(decrypted_payload):
    # Try decoding with UTF-8
    try:
        decrypted_payload_str_utf8 = decrypted_payload.decode("utf-8", errors="ignore")
    except UnicodeDecodeError:
        decrypted_payload_str_utf8 = ""

    # Try decoding with UTF-16
    try:
        decrypted_payload_str_utf16 = decrypted_payload.decode("utf-16", errors="ignore")
    except UnicodeDecodeError:
        decrypted_payload_str_utf16 = ""

    # Combine both decoded strings
    decrypted_payload_str = decrypted_payload_str_utf8 + decrypted_payload_str_utf16

    # Use regex to find HTTP URLs
    http_urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', decrypted_payload_str)
    
    return http_urls

def main():
    # Define the key
    key = bytes.fromhex("83 08 DF D6 68 7C 54 40 0F 1A 06 C9 DC C1 24 71 1A A3 EE 0D 9D 53 74")
    
    # Read the entire file
    with open("oligochaete.exe", "rb") as file:
        data = file.read()
        
        # Find the program section start
        program_section_start = bytes.fromhex("CE0052004F00D6006B")
        program_index = data.find(program_section_start)
        
        if program_index != -1:
            # Extract the program section
            program_section = data[program_index: program_index + 0x9c00 * 2]

            # Read every alternate byte
            program_section = program_section[::2]

            print("Program Section Length:", len(program_section))

            # Repeat the key to match the length of the program section
            repeated_key = (key * (len(program_section) // len(key) + 1))[:len(program_section)]

            # Perform XOR operation
            output = xor_bytes(program_section, repeated_key)

            # Write the output to "decrypted_payload.bin"
            with open("decrypted_payload.bin", "wb") as output_file:
                output_file.write(output)
            
            # Find HTTP strings in decrypted payload
            with open("decrypted_payload.bin", "rb") as decrypted_file:
                decrypted_payload = decrypted_file.read()
                http_strings = find_http_strings(decrypted_payload)

                # Print the found URLs
                if http_strings:
                    print("Malware Config (HTTP URLs):")
                    for url in http_strings:
                        print(url)
                else:
                    print("No malware config (HTTP URLs) found.")
        else:
            print("Program section not found in the file.")

if __name__ == "__main__":
    main()
