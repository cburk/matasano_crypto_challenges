from byte_ops import byte_iterator
from string_ops import do_nothing

failures = []

# TODO: If we're going anywhere with this, might as well make generic testing framework or use existing one

# Test 1: test ability to go byte by byte left, right
right_bytes = [0xde, 0xad, 0xbe, 0xef]
b = byte_iterator(0xdeadbeef, 0, 1, "right")
i = 0
try:
    while(1):
        byte = b.next()
        if byte != right_bytes[i]:
            failures.append("Test 1 failed @ byte: " + str(i) + ", expected byte: " + hex(right_bytes[i]) + ", got byte: " + hex(byte))
            break
        i += 1
except StopIteration:
    do_nothing()

b.new_num(0xdeadbeef, 0, 1, "left")
i = 0
try:
    while(1):
        byte = b.next()
        if byte != right_bytes[3 - i]:
            failures.append("Test 1 failed @ byte: " + str(i) + ", expected byte: " + hex(right_bytes[3 - i]) + ", got byte: " + hex(byte))
            break
        i += 1
except StopIteration:
    do_nothing()


# Report test results
num_f = len(failures)

if num_f == 0:
    print "All tests passed!"
else:
    print str(num_f) + " tests failed!"
    
    for failure in failures:
        print failure