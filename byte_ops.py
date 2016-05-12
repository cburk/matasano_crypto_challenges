from math import ceil, log
from matplotlib.pyplot import step

BYTE_SIZE =  8
ASCII_CHAR_SIZE = 8 # Remember, ascii chars are 1 byte each!

def num_bytes(num):
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
    return byte * pow(2, BYTE_SIZE * ind)

# While aligned returns 0xcc0000 for 0xccbbaa, get_byte just returns 0xcc
def get_byte(ind, num):
    new_num = num / pow(2, BYTE_SIZE * ind) # strip the last ind bytes away
    byte = new_num % pow(2, BYTE_SIZE)
    return byte

# Iterate over num step bytes at a time
# TODO: add option to get aligned byte or no, rn. it's not
class byte_iterator:
    def __init__(self, num, step):
        self.num = num
        self.step = step
        self.size = num_bytes(self.num)
        #print self.size
        self.i = 0
    
    def __iter__(self):
        return self
    
    def next(self):
        if(self.i == self.size):
            raise StopIteration
        else:
            res = 0
            for j in range(self.step):
                res += get_byte(self.i + j, self.num)
            
            self.i = self.i + self.step
            return res
        
# Repeat byte_seq until it is length bytes long.
def repeat_byte_sequence(byte_seq, length):
    seq_len = num_bytes(byte_seq)
    reps = length / seq_len
    partial = length % seq_len
    
    #print seq_len
    #print reps
    #print partial
    
    ret_str = 0
    for i in range(reps):
        ret_str += byte_seq * pow(2, BYTE_SIZE * seq_len * i) # TODO: Maybe make this pow(2, BYTE_SIZE * a generic function for alignment?
        
    for i in range(partial):
        print "got byte: " + hex(get_byte_aligned(i, byte_seq))
        print "pos: " + hex(pow(2, BYTE_SIZE * (reps + i)))
        ret_str += get_byte_aligned(i, byte_seq) * pow(2, BYTE_SIZE * ((seq_len * reps) + i))
        
    #print "repeated: " + hex(ret_str)
        
    return ret_str


