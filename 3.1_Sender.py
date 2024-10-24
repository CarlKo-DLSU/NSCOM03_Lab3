import socket

def send_checksum(int_array):
    # Assume the last element is to be replaced with the checksum
    int_values = int_array[:-1]  # All but the last element

    # Sum all the integer values
    total_sum = sum(int_values)

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

    # Replace the last element with the one's complement
    int_array[-1] = ones_complement

    return int_array

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = ('localhost', 65432)

    # Connect to the server
    client_socket.connect(server_address)

    # Get user input
    input_string = input("Enter integers separated by spaces: ")
    int_array = list(map(int, input_string.split()))  # Convert input to a list of integers

    # Ensure the last number is ignored and replaced with 0
    if len(int_array) > 0:
        int_array[-1] = 0  # Replace the last number with 0

    output_array = send_checksum(int_array)
    print("Sent data: " + str(output_array))

    # Send the output to the receiver
    client_socket.sendall(' '.join(map(str, output_array)).encode())

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()