from byte_ops import byte_iterator, num_bytes, repeat_byte_sequence

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
            score -= 10
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
    iter = byte_iterator(num, 1)
    ret_str = ""
    try:
        while(1):
            #print hex(b.next())
            ret_str += chr(iter.next())
    except StopIteration:
        do_nothing()
        #print "iteration complete"
        
    return ret_str[::-1]

def likely_single_xor(my_string):
    """
    Returns a list of the (5) character that was most likely to have been xor'ed w/ an english string to produce my_string
    (as well as the plaintext produced adn teh score of the english string)
    """
    #print "Encrypted str: " + ascii_int_to_str(my_string)

    likelys = []
    scores = [float("-inf")] # So that all scores are greater than it
    plaintexts = []
    #length = len(my_string)
    length = num_bytes(my_string)
    
   
    # Try all possible values for a single ascii char
    for this_char in range(10, 256):
        # Repeat this 2 bytes until it's same num bytes as my_string
        xor = repeat_byte_sequence(this_char, length)
        plain = ascii_int_to_str(my_string ^ xor)
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
    return [plaintexts[0], likelys[0], scores[0]]
