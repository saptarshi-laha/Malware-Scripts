# Function to generate key
def generate_key(string_to_generate_key):
    key_length = len(string_to_generate_key)
    key = []
    for i in range(key_length):
        key.append(ord(string_to_generate_key[i]) ^ (key_length - i))
    return key

# Function to perform XOR operation
def xor_data(data, key):
    output = []
    key_index = 0
    for i in range(len(data)):
        output.append(data[i] ^ key[key_index])
        if i == 0:
            key_index += 3
    return output

# Function to convert hex string to list of integers
def hex_string_to_int_list(hex_string):
    hex_list = hex_string.strip().split(" ")
    int_list = [int(hex_value, 16) for hex_value in hex_list]
    return int_list

# Function to convert list of integers to ASCII string
def int_list_to_ascii_string(int_list):
    ascii_string = ''.join([chr(value) for value in int_list])
    return ascii_string

# Main function
def main():

    config_data = "5F 5D 10 05 12 13 09 0B 0D 0F 0E 0B 09 05 19 57 04 12 0F 0E 05 4E 03 0F 0D 1C 6D 6A 58 5D 2E 0F 6D 6A 51 51 5D 24 01 12 0B 27 01 14 05 6D 6A 51 52 5D 32 50 09 0A 33 50 11 23 36 29 34 14 33 50 05 56 18 05 3A 6D 6A 51 53 5D 56 6D 6A 51 54 5D 39 05 13 6D 6A 51 55 5D 58 50 6D 6A 51 5D 39 05 13 6D 6A 53 5D 39 05 13 6D 6A 54 5D 2E 0F 6D 6A 51 58 5D 55 50 6D 6A 56 5D 2E 0F 6D 6A 57 5D 2E 0F 6D 6A 51 59 5D 57 50 50 50 6D 6A 55 5D 2E 0F 6D 6A 52 51 5D 2E 0F 6D 6A 52 52 5D 2E 0F 6D 6A 52 53 5D 39 05 13 6D 6A 52 55 5D 01 04 0D 09 0E 58 58 58 6D 6A 52 56 5D 2E 0F 6D 6A 52 57 5D 2F 2A 19 14 27 12 2E 25 6D 6A 52 58 5D 2E 0F 6D 6A 52 59 5D 56 6D 6A 14 01 02 0C 01 5D 36 06 32 0C 28 51 0A 09 17 1D 4A 5D 50 27 59 34 25 2F 11 12 52 3A 2C 31 53 39 54 37 03 3D 48 15 19 04 0E 44 33 13 16 0D 14 57 23 4E 4C 3B 2A 22 2E 08 38 1A 02 42 0B 01 18 46 10 26 2B 58 0F 55 35 07 24 21 49 56 29 2D 40 05 30 1B 6D 6A 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"  # Fill this with your actual config_data

    string_to_generate_key = "ckcilIcconnh"  # Fill this with your actual string_to_generate_key

    # Convert hex string to list of integers
    data = hex_string_to_int_list(config_data)

    # Generate key
    key = generate_key(string_to_generate_key)

    # XOR data with key
    output = xor_data(data, key)

    # Convert list of integers to ASCII string
    output_ascii_string = int_list_to_ascii_string(output)
    key_ascii_string = int_list_to_ascii_string(key)

    print("Generated Key (ASCII):", key_ascii_string)
    print("XORed Output (ASCII):", output_ascii_string)



if __name__ == "__main__":

    main()

