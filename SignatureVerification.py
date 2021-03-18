from ECDSA import *

#Input for signature validation
inp = str(input("Enter Your Messgae : "))
msg = bytes(inp, encoding="utf-8")

if len(msg) == 0:
    print("You have not entered anything!")
else:
    #Public Key Expansion
    inp1,inp2 = input("Enter Your Public Key : ").split(', ')
    keys = [int(inp1),int(inp2)]
    keys = tuple( keys )

    #Input Signature Expansion
    sign1, sign2 = input("Enter The Signature :").split(", ")
    sign1, sign2 = int(sign1), int(sign2)
    inp_signature = [hex(sign1), hex(sign2)]

    if len(keys) <= 1 or len(inp_signature) <= 1:
        print("Incorrect Inputs...!")
        exit()
    else:
        #print(keys)
        #print(inp_signature)
        #print(verify_signature(keys, msg, inp_signature))
        if ( verify_signature ( keys , msg , inp_signature ) ) :
            print(" Valid Signature...! ")
        else :
            print(" Invalid Signature...!")
