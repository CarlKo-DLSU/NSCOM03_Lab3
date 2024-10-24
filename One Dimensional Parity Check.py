signal = [1,0,0,1,0,1,0,0,1]
parity_bit = 1

count = 0
for i in signal:
    if i == 1:
        count += 1

print(f"-- Odd Parity --")
print(f"Number of 1's: {count}")
if count % 2 > 0:
    print("No errors detected\n")
else:
    print("Error detected\n")

print(f"-- Even Parity --")
print(f"Number of 1's: {count}")
if count % 2 == 0:
    print("No errors detected\n")
else:
    print("Error detected\n")