import socket

def send_checksum(input_string):
    # Split the input into the string part and the number part
    parts = input_string.split()
    if len(parts) != 2:
        raise ValueError("Input must contain a string and a number separated by a space.")
    
    text = parts[0]  # The string part
    number = int(parts[1])  # The number part

    # Convert each character in the string to its ASCII value
    ascii_values = [ord(char) for char in text]

    total_sum = sum(ascii_values)

    # Convert the sum to binary and remove the first two bits
    bin_sum = bin(total_sum)[2:]  # binary representation of the sum (removes the '0b' prefix)
    if len(bin_sum) > 2:
        removed_bits = bin_sum[:2]
        remaining_bits = bin_sum[2:]
    else:
        removed_bits = bin_sum
        remaining_bits = ''

    # Treat the removed bits as a new 2-bit number
    removed_bits_value = int(removed_bits, 2) if removed_bits else 0
    remaining_value = int(remaining_bits, 2) if remaining_bits else 0

    # Use logical addition (bitwise OR) instead of arithmetic addition
    checksum_value = removed_bits_value | remaining_value

    # Calculate the maximum value based on the larger number of bits
    num_bits = max(len(removed_bits), len(remaining_bits)) if (removed_bits or remaining_bits) else 1  # Ensure at least 1 bit
    max_value = (1 << num_bits) - 1  # 2^num_bits - 1

    # Calculate the one's complement of the checksum value
    ones_complement = (max_value - checksum_value) & max_value

    # Return the original string and the checksum
    return f"{text} {ones_complement}"

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = ('localhost', 65432)

    # Connect to the server
    client_socket.connect(server_address)

    # Get user input
    input_string = input("Enter a string and a number separated by a space: ")
    output_string = send_checksum(input_string)
    print("Sent data: " + str(output_string))

    # Send the output to the receiver
    client_socket.sendall(output_string.encode())

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()