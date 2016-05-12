from string_ops import likely_single_xor

#Find single encrypted line and it's plaintext in a file

f = open("../files/4ciphertexts", "r")

print f

line = f.readline()
i = 0
best = [[float("-inf"), float("-inf"), float("-inf")]]
for line in f:
    int_repr = int(line, 16)
    likely = likely_single_xor(int_repr)
    for j in range(5):
        if likely[2] > best[j][2]:
            best.insert(j, likely)
            break
    i = i + 1
    
print best[:5]    
#Answer: now the party is jumping
