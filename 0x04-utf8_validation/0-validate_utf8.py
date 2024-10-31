#!/usr/bin/python3
"""
Function to determine if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7     # 10000000 in binary
    mask2 = 1 << 6     # 01000000 in binary

    # Iterate over each integer (representing a byte)
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1s in the byte
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            """For a single-byte character (0xxxxxxx) or if the number of
            bytes is more than 4, it's invalid"""
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the next byte is in the format 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the count of remaining bytes
        num_bytes -= 1

    return num_bytes == 0
