#Author - ExploitedSite

import sys
import struct
import lznt1

def main(input_png_file, output_bin_file):
    try:
        # Step 1: Read input PNG file
        with open(input_png_file, 'rb') as f:
            png_data = f.read()

        # Step 2: Parse IDAT sections and extract data
        idat_sections = [b'IDAT']
        buffer = b''
        idat_count = 0
        buf_disc_len = 0

        for section in idat_sections:
            start_idx = png_data.find(section)
            while start_idx != -1:
                idat_count += 1
                length_data = struct.unpack('>I', png_data[start_idx - 4:start_idx])[0]
                data = png_data[start_idx + 4:start_idx + length_data + 4]  # Include the section length bytes

                if idat_count == 3:
                    xor_key = data[4:8]  # Extract XOR key from the third IDAT section
                    buf_disc_len = len(buffer)

                buffer += data
                start_idx = png_data.find(section, start_idx + length_data + 4)



        if idat_count < 3:
            raise ValueError("Less than 3 IDAT sections found")

        # Exclude null bytes at the end of the last IDAT section
        null_bytes_start = buffer.find(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        if null_bytes_start != -1:
            buffer = buffer[:null_bytes_start]

        buffer = buffer[buf_disc_len+16:]

        # Step 3: XOR buffer with key bytes cyclically
        xor_key_bytes = bytearray(xor_key)
        xored_buffer = bytearray()

        for i in range(0, len(buffer), 4):
            block = buffer[i:i + 4]
            xored_block = bytes(x ^ xor_key_bytes[j] for j, x in enumerate(block))
            xored_buffer.extend(xored_block)

        remaining_bytes = len(buffer) % 4
        if remaining_bytes != 0:
            xored_buffer.extend(buffer[-remaining_bytes:])  # Append remaining bytes as is

        xored_buffer = bytes(xored_buffer)

        # Step 4: Decompress xored_buffer using LZNT1
        decompressed_data = lznt1.decompress(xored_buffer)

        # Step 5: Write decompressed data to output bin file
        with open(output_bin_file, 'wb') as f:
            f.write(decompressed_data)

        print("Decompression and writing successful.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Attempting to dump by brute forcing buffer length.")
        counter = 0
        for counter in range(100):
            try:
                xored_buffer_1 = xored_buffer[:len(xored_buffer)-counter]
                decompressed_data = lznt1.decompress(xored_buffer_1)

                with open(output_bin_file, 'wb') as f:
                    f.write(decompressed_data)

                break
            except Exception as e1:
                counter+=1

        if counter >= 100:
            print("Failed to dump correct buffer. Dumping XORed buffer.")
            with open(output_bin_file, 'wb') as f:
                f.write(xored_buffer)
        else:
            print("Decompression and writing successful.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.png output.bin")
    else:
        input_png_file = sys.argv[1]
        output_bin_file = sys.argv[2]
        main(input_png_file, output_bin_file)