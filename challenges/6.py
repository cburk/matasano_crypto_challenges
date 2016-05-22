from byte_ops import hamming_dist, num_bytes
from string_ops import str_to_ascii_int, likely_repeating_xor, ascii_int_to_str,\
    repeating_key_encrypt
from converter import base642num
from time import sleep

st1 = "this is a test"
st2 = "wokka wokka!!!"

# print hamming_dist(str_to_ascii_int(st1), str_to_ascii_int(st2))
# Answer: 37, appears to be working fine

#print "Original: " + ascii_int_to_str(0x48656C6C6F495051525354)
#print likely_repeating_xor(0x48656C6C6F495051525354)



# Coming up w/ correct keys, just needs scoring and modifications (normalization?) to hd
# WORKS!  Testcase?
#hex = 0x0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
#print "Original: " + ascii_int_to_str(hex)
#print likely_repeating_xor(hex)

# TEST !
plaintexts = ["I saw the best minds of my generation destroyed by madness, starving hysterical naked, dragging themselves through the negro streets at dawn looking for an angry fix, angelheaded hipsters burning for the ancient heavenly connection to the starry dynamo in the machinery of night, who poverty and tatters and hollow-eyed and high sat up smoking in the supernatural darkness of cold-water flats floating across the tops of cities contemplating jazz, who bared their brains to Heaven under the El and saw Mohammedan angels staggering on tenement roofs illuminated, who passed through universities with radiant cool eyes hallucinating Arkansas and Blake-light tragedy among the scholars of war, who were expelled from the academies for crazy & publishing obscene odes on the windows of the skull, who cowered in unshaven rooms in underwear, burning their money in wastebaskets and listening to the Terror through the wall, who got busted in their pubic beards returning through Laredo with a belt of marijuana for New York, who ate fire in paint hotels or drank turpentine in Paradise Alley, death, or purgatoried their torsos night after night with dreams, with drugs, with waking nightmares, alcohol and cock and endless balls, incomparable blind streets of shuddering cloud and lightning in the mind leaping toward poles of Canada & Paterson, illuminating all the motionless world of Time between",
"In the beginning, God created the earth, and he looked upon it in His cosmic loneliness.And God said, Let Us make living creatures out of mud, so the mud can see what We have done. And God created every living creature that now moveth, and one was man. Mud as man alone could speak. God leaned close to mud as man sat up, looked around, and spoke. Man blinked. What is the purpose of all this? he asked politely.Everything must have a purpose? asked God.Certainly, said man.Then I leave it to you to think of one for all this, said God. And He went away.",
"MANY years ago, I contracted an intimacy with a Mr. William Legrand. He was of an ancient Huguenot family, and had once been wealthy; but a series of misfortunes had reduced him to want. To avoid the mortification consequent upon his disasters, he left New Orleans, the city of his forefathers, and took up his residence at Sullivan's Island, near Charleston, South Carolina."
]

# Almost correct if bach spelled this way, oddly incorrect if spelled correctly
# TODO: Obvi could step by step, but also look at lengths of keys in relation to len of plaintexts.
#keys = ["ESCHER", "GODEL", "BACHE"]
keys = ["ESCHER", "GODEL", "BACH"]

for i in range(3):
    pt = plaintexts[i]
    k = keys[i]
    
    enc_hex = repeating_key_encrypt(pt, k)
    
    print "Encrypted: " + hex(enc_hex)
    #0xf000d116238262930326329252e6f680b6120272c3531292135262c62202d682b2f37212f20203162362a3c2a6122680f336d6815282f242b202e680e24243a232f276662092668352030682d2763292c6122262128262636610b3d253426262d35632e232c2a243b6d63292c256320232563272c22266820242626623626292e352b317961213d36612268312431212732632724612e2131272c3a36342d2d31612b292661312d2634202d26612b212f61372762362226366f631c2d61223e2d282768362926682f2e313c2b272a2b23352a272c6120272c32263937242d3c623433272c612b21316127213120303c27333064622926682e24253c620f263f620e312427202d3b6e613720276120213638632724612b2131612527302425293629263a316d63292c25633c2d2e2868373163202b32633a27322a2c272f202d6220376811342f242b37222665326301312d2226266d6326272031680129223a2e24303c2d2f6f68112e363c2a610029302e2f212c206dL

    likely_repeating_xor(enc_hex)
    
    #sleep(5)


"""

# Read the file
f = open("../textfiles/6.txt", "r")

#TODO: Are \n an issue here?
b64 = ""
for line in f:
    print line[:-1] + " ::: "
    b64 += line[:-1]
    if b64[-1] == '\n':
        print "ERROR! Newline!"

#TODO: Add this to normal b64 decode?
missing_padding = 4 - len(b64) % 4
for i in range(missing_padding):
    b64 += '='
    
print "Finished: "
print b64

# Decode BASE64
#ciphertextnum = base642num(b64)
ciphertextnum = base642num(b64)
print hex(ciphertextnum)

# find repeating key and pt
print likely_repeating_xor(ciphertextnum)

"""