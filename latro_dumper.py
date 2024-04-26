import re

def xor_bytes(bytes1, bytes2):
    return bytes(a ^ b for a, b in zip(bytes1, bytes2))

def main():
    # Define the key
    key = bytes.fromhex("65 64 6d 4f 42 74 69 75 64 66 29 4f 5a 6f 24 4c 42 2b 00")
    
    # Read the entire file
    with open("mbaeapina.dll", "rb") as file:
        data = file.read()
        
        # Find the program section start
        program_section_start = bytes.fromhex("283EFD4F417469756066294FA59024")
        program_index = data.find(program_section_start)
        
        if program_index != -1:
            # Extract the program section
            program_section = data[program_index: program_index + 0x11900]

            # Read every byte
            program_section = program_section[::1]

            print("Program Section Length:", len(program_section))

            # Repeat the key to match the length of the program section
            repeated_key = (key * (len(program_section) // len(key) + 1))[:len(program_section)]

            # Perform XOR operation
            output = xor_bytes(program_section, repeated_key)

            # Write the output to "decrypted_payload.bin"
            with open("latro_dumped.bin", "wb") as output_file:
                output_file.write(output)
            
        else:
            print("Program section not found in the file.")

if __name__ == "__main__":
    main()