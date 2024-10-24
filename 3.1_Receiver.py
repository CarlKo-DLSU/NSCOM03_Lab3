import socket

def receive_checksum(int_array):
    # Sum all the integer values
    total_sum = sum(int_array)

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

    return ones_complement

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = ('localhost', 65432)

    # Bind the socket to the server address and port
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    print("Server listening for incoming connections...")

    # Wait for a connection
    connection, client_address = server_socket.accept()

    try:
        print("Connection from", client_address)

        # Receive data from the sender
        data = connection.recv(1024).decode()
        print("\nReceived data: " + str(data))

        # Convert the received data into an array of integers
        int_array = list(map(int, data.split()))

        # Compute the checksum
        checksum = receive_checksum(int_array)

        # Print the result
        if checksum == 0:
            print("Output: " + str(checksum) + " | No Errors Detected")
        else:
            print("Output: " + str(checksum) + " | Error Detected!")

    finally:
        # Close the connection
        connection.close()
        # Close the server socket
        server_socket.close()
        print("Server closed after processing the connection.")

if __name__ == "__main__":
    main()