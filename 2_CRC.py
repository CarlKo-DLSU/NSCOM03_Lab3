def xor(dividend, divisor):
    """Perform XOR operation between two binary strings."""
    result = []
    for i in range(len(divisor)):
        result.append('0' if dividend[i] == divisor[i] else '1')
    return ''.join(result)

def crc_division(data, divisor):
    """Perform CRC division and return the remainder."""
    # Append zeros to the data
    data = data + '0' * (len(divisor) - 1)
    
    # Convert to list for easier manipulation
    data = list(data)
    divisor = list(divisor)
    
    # Perform the division
    for i in range(len(data) - len(divisor) + 1):
        if data[i] == '1':  # Only perform XOR if the leading bit is 1
            # Perform XOR with the divisor
            data[i:i + len(divisor)] = xor(data[i:i + len(divisor)], divisor)
    
    # The remainder is the last (len(divisor) - 1) bits of the data
    remainder = ''.join(data[-(len(divisor) - 1):])
    return remainder

def main():
    # Input binary data and divisor separated by space
    user_input = input("Enter binary frame and generator separated by a space: ")
    data, divisor = user_input.split()  # Split the input into data and divisor

    # Perform CRC division
    remainder = crc_division(data, divisor)

    # Concatenate the remainder to the original data
    transmitted_data = data + remainder

    # Output the result
    print(f"Remainder: {remainder}")
    print(f"Transmitted Data: {transmitted_data}")

if __name__ == "__main__":
    main()