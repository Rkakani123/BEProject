from ECDSA import *

#print("Curve: {}".format(curve.name))
#input for signature
input_msg = str(input("Enter Your Message : "))
msg = bytes(input_msg, encoding='utf-8')

if len(msg) == 0:
    print("You have not entered anything!")
else:
    #Key generation
    private, public = make_keypair()
    print(public)

    #Signature Generation
    signature = sign_message(private, msg)
    print(signature)
