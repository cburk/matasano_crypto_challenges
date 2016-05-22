from math import ceil, log
from matplotlib.pyplot import step

BYTE_SIZE =  8
ASCII_CHAR_SIZE = 8 # Remember, ascii chars are 1 byte each!

# TODO: Update for case w/ 0.  Should we just be passing that info in to byte iterator or something?
def num_bytes(num):
    # TODO: Change this after we figure out a more permanent solution
    if num == 0:
        return 1
    
    return int(ceil(log(num, 2)/BYTE_SIZE))
    #return int(ceil(log(num, 16))/2)

# Get the ind'th byte from num, where 0 is the last byte (i.e. nums from 0 -> 2 ^ 8)
def get_byte_aligned(ind, num):
    #print hex(num)
    new_num = num / pow(2, BYTE_SIZE * ind) # strip the last ind bytes away
    #print hex(new_num)
    byte = new_num % pow(2, BYTE_SIZE)
    #print hex(byte)
    #multiply it back out to its original position
    return int(byte * pow(2, BYTE_SIZE * ind))

# While aligned returns 0xcc0000 for 0xccbbaa, get_byte just returns 0xcc
def get_byte(ind, num):
    new_num = num / pow(2, BYTE_SIZE * ind) # strip the last ind bytes away
    byte = new_num % pow(2, BYTE_SIZE)
    return int(byte)

# Iterate over num step bytes at a time
# TODO: add option to get aligned byte or no, rn. it's not
class byte_iterator:
    def __init__(self, num, start, step, direction):
        self.num = num
        self.start = start
        self.step = step
        self.size = num_bytes(self.num)
        self.dir = direction
        #print self.size
        self.i = start # TODO: Should i be something not 0 if we start at start?  ex. start if dir = right, i - start
    
    def __iter__(self):
        return self
        
    # Basically reset byte_terator w/ new definitions, saves an object creation
    def new_num(self, new_num, start, step, direction):
        self.num = new_num
        self.size = num_bytes(new_num)
        self.start = start
        self.step = step
        self.dir = direction
        self.i = start
    
    def next(self):
        if(self.i == self.size):
            raise StopIteration
        else:
            res = 0
            # If there's not a full step's worth of bytes to traverse, just do the last ones
            if(self.i + self.step > self.size):
                num_traverse = self.size - self.i
            else:
                num_traverse = self.step
            
            #for j in range(self.size):
            for j in range(num_traverse):
                if self.dir == "left":
                    #res += get_byte(self.i + j + self.start, self.num)
                    res += get_byte(self.i + j + self.start, self.num) * pow(2, BYTE_SIZE * j)
                else:
                    #res += get_byte(self.size - (self.i + j + 1 + self.start), self.num)
                    #res += get_byte(self.size - (self.i + j + 1 + self.start), self.num) * pow(2, BYTE_SIZE * (num_traverse - j - 1))
                    res += get_byte(self.size - (self.i + j + 1), self.num) * pow(2, BYTE_SIZE * (num_traverse - j - 1))

            #self.i = self.i + self.step
            self.i = self.i + num_traverse
            return res

# TODO: I think for sequences of size > 1, process happens in reverse.  Should use byte iterator instead
# Repeat byte_seq until it is length bytes long.
def repeat_byte_sequence2(byte_seq, length):
    ret = 0
    seq_len = num_bytes(byte_seq)
    reps = length / seq_len
    partial = length % seq_len
    pos = length - 1
    
    for i in range(reps):
        b = byte_iterator(byte_seq, 0, 1, "right") #TODO: Make it w/o so much object creation, maybe a reset option in iterator?
        for j in range(seq_len):
            ret += b.next() * pow(2, BYTE_SIZE * pos)
            pos -= 1
        
    b = byte_iterator(byte_seq, 0, 1, "right")
    for i in range(partial):
        ret += b.next() * pow(2, BYTE_SIZE * pos)
        pos -= 1
    
    return ret

# Maybe come back to this later, but seems broken, 2 is using byte iterator which seems better than math w/ getbyte anyways
"""
def repeat_byte_sequence(byte_seq, length):
    seq_len = num_bytes(byte_seq)
    reps = length / seq_len
    partial = length % seq_len
        
    ret_str = 0
    for i in range(reps):
        ret_str += byte_seq * pow(2, BYTE_SIZE * seq_len * i) # TODO: Maybe make this pow(2, BYTE_SIZE * a generic function for alignment?
        
    for i in range(partial):
        ret_str += get_byte(i, byte_seq) * pow(2, BYTE_SIZE * ((seq_len * reps) + i))
        
    #print "repeated: " + hex(ret_str)
        
    return ret_str
"""

# Returns the number of differing bits between the two sequences of equal length.
# TODO: If i think of an easy way to do this that doesn't cheat by counting 1's in string rep
def hamming_dist(a, b):
    c = a ^ b
    count = 0
    for bit in bin(c):
        if bit == '1':
            count += 1
    return count

def normalized_hamming_dist(a, b):
    return hamming_dist(a, b) / float(num_bytes(a))

# Returns a list containing num broken up into chunks of size bytes
# Ex. byte_partition(0xdeadbeef, 2) = [0xdead, 0xbeef]
def byte_partition(num, size):
    ret = []
    b = byte_iterator(num, 0, size, "right")
    try:
        while(1):
            ret.append(b.next())
    except StopIteration:
        print "iteration complete"
    
    return ret

# Returns the list of bytes compiled into one number, ex. [0xde, 0xad, 0xbe, 0xef] -> 0xdeadbeef
def byte_concat(byte_list):
    ret = 0
    num_bytes = len(byte_list)
    j = 0
    for byte in byte_list:
        ret += byte * pow(2, BYTE_SIZE * (num_bytes - (1 + j)))
        j += 1

    return ret