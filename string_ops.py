from byte_ops import byte_iterator, num_bytes, repeat_byte_sequence2, hamming_dist, byte_partition, byte_concat
from time import sleep

def do_nothing():
    return

def score(my_string):
    """
    Score a string on how likely it is to be an english sentence
    """
    scores = {'etoain shrdluETOAINSHRDLU': 4, 'cmwfgypbCMWFGYPB': 2, 'VKJXAZvkjxqz\'"': 1, '.!(),?1234567890': -2}
    score = 0
    for c in my_string:
        english = False
        for letter_group in scores:
            if c in letter_group:
                score += scores[letter_group]
                english = True
        if not english:
            #score -= 2
            score -= 40
    return score

def repeat_sequence(my_seq, size):
    """
    Returns the sequence my_string repeated until it's size long
    Ex. abc, 11 = abcabcabcab
    """
    seq_len = len(my_seq)
    reps = size / seq_len
    partial = size % seq_len
    
    ret_str = ""
    for i in range(reps):
        ret_str += my_seq
        
    for i in range(partial):
        ret_str += my_seq[i]
        
    return ret_str

def ascii_int_to_str(num):
    """
    Given an int representation of an ascii string (ex. 0x414243)
    returns the english representation (above ex, "ABC")
    
    TODO: May have to reverse
    """    
    iterat = byte_iterator(num, 0, 1, "right")
    ret_str = ""
    try:
        while(1):
            #print hex(b.next())
            ret_str += chr(iterat.next())
    except StopIteration:
        do_nothing()
        #print "iteration complete"
        
    #return ret_str[::-1]
    return ret_str

def str_to_ascii_int(my_string):
    """
    Reverse of ascii_int_to_str
    """
    ret = 0
    pos = len(my_string) - 1
    for c in my_string:
        ret += ord(c) * pow(2, 8 * pos)
        pos -= 1
    
    return ret

def likely_single_xor(string_num):
    """
    Returns a list of the character that was most likely to have been xor'ed w/ an english string
    to produce string_num (which is here represented as an integer).
    Also returns the plaintext produced adn teh score of the english string
    """
    print "Encrypted str: " + ascii_int_to_str(string_num)

    likelys = []
    scores = [float("-inf")] # So that all scores are greater than it
    plaintexts = []
    #length = len(string_num)
    length = num_bytes(string_num)
    
   
    # Try all possible values for a single ascii char
    # TODO: For these exercises, i've limited the possible keys to visible chars.  Not a valid assumption for other purposes
    #for this_char in range(10, 256):
    for this_char in range(41, 123):
        # Repeat this 2 bytes until it's same string_num bytes as string_num
        xor = repeat_byte_sequence2(this_char, length)
        plain = ascii_int_to_str(string_num ^ xor)
        #print "XOR'ed w/: " + chr(this_char) +  " = " + plain
        
        this_score = score(plain)
        #print "score: " + str(this_score)
        
        for i in range(5):
            if this_score > scores[i]:
                likelys.insert(i, this_char)
                scores.insert(i, this_score)
                plaintexts.insert(i, plain)
                break

    #return [plaintexts[:5], likelys[:5], scores[:5]]
    #return [plaintexts[:10], likelys[:10], scores[:10]]
    return [plaintexts[0], likelys[0], scores[0]]


def likely_repeating_xor(str_num):
    hamming_dists = [float("inf"), float("inf"), float("inf"), float("inf"), float("inf")]
    keysizes = []
    pts = []
    keys = []
    scores = [float("-inf"), float("-inf"), float("-inf")]
    total_bytes = num_bytes(str_num)

    # Find the most likely keysize used to encrypt this passage based on hamming distance of byte groups
    for keysize in range(1, 20):
        this_dist = 0
        a = byte_iterator(str_num, 0, 1, "right")
        b = byte_iterator(str_num, keysize, 1, "right")
        
        print "Keysize: " + str(keysize)
        """
        for i in range(keysize):
            a1 = a.next()
            b1 = b.next()
            print hex(a1) + " vs " + hex(b1) + " = " + str(hamming_dist(a1, b1))
            this_dist += hamming_dist(a1, b1)
        """
        
        # TODO: Maybe need to undo this, but checking over two/3 sample areas and averaging, b/c seems kinda innacurate to just do one section
        start_pts = [total_bytes/3, total_bytes/2, total_bytes/4]
        for j in start_pts:
            a.new_num(str_num, j, 1, "right")
            b.new_num(str_num, j + keysize, 1, "right")

            for i in range(keysize):
                a1 = a.next()
                b1 = b.next()
                print hex(a1) + " vs " + hex(b1) + " = " + str(hamming_dist(a1, b1))
                this_dist += hamming_dist(a1, b1)

        this_dist /= float(keysize)
        # TODO: Might have to undo normalization, part of above
        this_dist /= len(start_pts)
        
        for i in range(5):
            if this_dist < hamming_dists[i]:
                hamming_dists.insert(i, this_dist)
                keysizes.insert(i, keysize)
                break
            
    print "Keysizes: Dists"
    print keysizes
    print hamming_dists
    sleep(5)
    
    # Take only the best
    o_keysizes = keysizes
    o_hamming_dists = hamming_dists
    keysizes = keysizes[:4] #TODO: Set back to 2
    hamming_dists = hamming_dists[:4] # sSet backt o2
    
    # Find likely key for each keysize
    for i in range(3): #TODO set bakc to 2
        keysize = keysizes[i]
        print "keysize: " + str(keysize)
        chunks = byte_partition(str_num, keysize)
        
        print "bp: " + str(chunks)
        
        # Make groups of the j'th bytes in each chunk
        by_byte = []
        for j in range(keysize):
            by_byte.append([])
        b = byte_iterator(0xdeadbeef, 0, 1, "right") #placeholder
        for j in range(len(chunks)):
            this_chunk = chunks[j]
            b.new_num(this_chunk, 0, 1, "right")
            for k in range(num_bytes(this_chunk)):
                this_byte = b.next()
                by_byte[k].append(this_byte)
        
        print "by bytes: " + str(by_byte)

        # Concatenate lists of bytes into one number, so we can decrypt w/ single key xor
        for j in range(keysize):
            by_byte[j] = byte_concat(by_byte[j])
            print "All " + str(j) + " bytes: " + hex(by_byte[j])
        
        # Recreate the key using result of decryption for each num in by_byte
        results = []
        key = ""
        for j in range(keysize):
            results.append(likely_single_xor(by_byte[j]))
            print results[j]
            key += chr(results[j][1])
            
        # TODO: Investigate, but should probs just replace rbs w/ rbs2
        ciphertextnum = repeat_byte_sequence2(str_to_ascii_int(key), num_bytes(str_num))
        #print "\ndecrypting..."
        #print hex(ciphertextnum)
        #print hex(str_to_ascii_int(key))
        #print hex(str_num)
        plaintextnum = ciphertextnum ^ str_num
        plaintext = ascii_int_to_str(plaintextnum)
        #print "Found key: " + key + " , resulting decrypt: " + plaintext
        
        # Score plaintexts, order
        # TODO: Make own order function?
        this_score = score(plaintext)
        for i in range(3):
            if this_score >= scores[i]:
                scores.insert(i, this_score)
                pts.insert(i, plaintext)
                keys.insert(i, key)
                break

    #print o_hamming_dists
    #print o_keysizes
    
    print "Found pts: "
    for pt in pts:
        print pt
    print "W/ keys: " + str(keys)
    print "W/ scores: " + str(scores)
    
    return 0


def repeating_key_encrypt(plaintext, key):
    plain_hex = str_to_ascii_int(plaintext)
    key_hex = str_to_ascii_int(key)
    cipher_hex = repeat_byte_sequence2(key_hex, len(plaintext))
    cipher_text_hex = cipher_hex ^ plain_hex
    
    return cipher_text_hex