from string_ops import likely_single_xor

#print len("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

#print num_bytes(0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736)
#print num_bytes(0xaabbccdd)
#print num_bytes(0xaabbccddaabbccdd)

#print "getting second byte of 0xaabbccddaabbccdd"
#print hex(get_byte(2, 0xaabbccddaabbccdd))

#print "getting third byte of 0xaabbccddf3bbccdd"
#print hex(get_byte(3, 0xaabbccddf3bbccdd))

# 1 to get every byte, 2 to get every 2 bytes (ascii char)
#b = byte_iterator(0xaabbccdea1b2, 1)
#try:
#    while(1):
#        print hex(b.next())
#except StopIteration:
#    print "iteration complete"



    
#b = byte_iterator(0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736, 1)
#try:
#    while(1):
#        print hex(b.next())
#except StopIteration:
#    print "iteration complete"

#print hex(repeat_byte_sequence(0xaabb, 6))
#print hex(repeat_byte_sequence(0xaabb, 9))

# Looks good, might have to reveres tho
#print ascii_int_to_str(0x004100420043)

# SEEMS TO ALL BE WORKING WELL UP TO HERE

#print hex(0xfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd ^ 0xfcfdfbfbfbfafafdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd)
print likely_single_xor(0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736)


# Answer: XOR'ed w/: X = Cooking MC's like a pound of bacon
