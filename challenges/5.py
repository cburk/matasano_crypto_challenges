from byte_ops import byte_iterator, repeat_byte_sequence, repeat_byte_sequence2
from string_ops import ascii_int_to_str, str_to_ascii_int


#for dir in ["right", "left"]:
#    b = byte_iterator(0xdeadbeef, 1, dir)

#    try:
#        while(1):
#            print hex(b.next())
#    except StopIteration:
#        print "iteration complete"


#print ascii_int_to_str(0x48656C6C6F)
#print hex(str_to_ascii_int("Hello"))
print ascii_int_to_str(str_to_ascii_int("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"))

plain_hex = str_to_ascii_int("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
ice_hex = str_to_ascii_int("ICE")
cipher_hex = repeat_byte_sequence2(ice_hex, len("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"))
cipher_text_hex = cipher_hex ^ plain_hex

print hex(plain_hex) #correct 
print hex(cipher_hex) #incorrect
print hex(ice_hex) #correct

print "RES: " + hex(cipher_text_hex)
"""
Expected: 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

Seems like it's working!
"""