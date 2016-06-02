

def calculate_primer_melting_temp(primer):
    temp = 0
    for base in primer:
        if base == 'c' or base == 'g':
            temp += 4
        elif base == 't' or base == 'a':
            temp += 2
    return temp

reverse = 'tctgaagtgatgcttgtctg'
forward = 'ggcctgttttgctatctgtc'

reverse_temp = calculate_primer_melting_temp(reverse)
forward_temp = calculate_primer_melting_temp(forward)


print("Reverse temp: " + str(reverse_temp))
print("Forward temp: " + str(forward_temp))