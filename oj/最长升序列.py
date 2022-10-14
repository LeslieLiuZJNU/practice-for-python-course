sequence = input()
temp_sequence = []
temp_length = 0
max_sequence = []
max_length = 0

for i in range(len(sequence)):
    temp_sequence.append(int(sequence[i]))
    temp_length = temp_length + 1
    if i == len(sequence) - 1 or int(sequence[i]) >= int(sequence[i + 1]):
        if temp_length > max_length:
            max_sequence = temp_sequence
            max_length = temp_length
        temp_sequence = []
        temp_length = 0

print(max_length)
print(max_sequence)
