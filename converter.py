
def num2base64(num):
    my_str = hex(num)[2:]
    if(len(my_str) % 2 != 0):
        my_str = my_str[:-1]
    #my_str = 
    return my_str.decode('hex').encode('base64')
    

def str2base64(my_str):
    return my_str.encode('base64')

def base642num(str64):
    new = str64.decode('base64').encode('hex')
    return int(new, 16)

def base642str(str64):
    return str64.decode('base64')


"""
def myhex2base64(num):
    # Conversion dictionary, 6 bit values -> base64 chars
    base64dict = {}

    for i in range(26):
        print "dict: " +  str(i) + " : " + chr(ord('A') + i)
        base64dict[i] = chr(ord('A') + i)
    
    for i in range(26):
        print "dict: " +  str(26 + i) + " : " + chr(ord('a') + i)
        base64dict[26 + i] = chr(ord('a') + i)

    for i in range(10):
        print "dict: " + str(i + 52) + " : " + str(i)
        base64dict[i + 52] = str(i)

    base64dict[62] = "+"
    base64dict[63] = "/"
    
    print str(bin(num))
    print "is this power? 8 vs: " + str(pow(2, 3))
    
    masks = []
    current = 0
    for i in range(len(bin(num))):
        if(i % 6 == 0 and i != 0):
            print "Mask " + str(i) + " is: " + str(current)
            masks.append(current)
            current = 0
            
        current += pow(2, i)
    
    masks.append(current)
    
    print str(bin(masks[2]/2))
    print str(bin(masks[2]/4))
    print str(bin(masks[2]/8))
    print str(bin(masks[2]/pow(2, len(bin(masks[2])) - 8)))

    
    # TODO: special case last chunk, problems if it's not a clean interval of 6
    # Might have fixed it
    encoded = ""
    i = 0
    for mask in masks:
        current = (mask & num) / pow(2, i)
        print "this six bytes: " + str(bin(current))
        #print "truncated: " + str(bin(current/pow(2, len(bin(mask)) - 8)))
        encoded += base64dict[current]
        i += 6
        
    encoded = encoded[::-1]
        
    #m1 = 0b111111
    #m2 = 0b111111000000
    #m3 = 0b111111000000000000
    #m4 = 0b111111000000000000000000
    #print str(m1) + " vs " + str(m2) + " vs " + str(m3) + " vs " + str(m4)
    #print "Partition: " + str(hex(m1 & num)) + " : " + str(hex(m2 & num)) + " : " + str(hex(m3 & num)) + " : " + str(hex(m4 & num))
    
    return encoded
    
def base642hex(num):
    return 0
"""

