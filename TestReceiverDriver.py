import AES
import Convert
from ECDSA import *
from ImageDecryption import *

#Input for Steg File
input_file = input("Enter File To Be Decoded : ")
#Unpacking Data Hidden in Steg File
msg = imageDecrypt(input_file)
msg = Convert.StringToDict(msg)

#Input For Decryption
#msg = eval(input("Enter The Text to be Decrypted : "))

#Cipher unbundling
#inp_sig = msg["Signature"]
inp_sig =  [msg["P"], msg["Q"]]
input_signature = [hex(int(inp_sig[0])) , hex(int(inp_sig[1]))]
EncryptedData = msg["Data"]

#Key Generation
private_key = int(input("Enter Your Shared Key : "))
public_key = scalar_mult(private_key, curve.g)

#AES Object Creation
aes = AES.AES(private_key)
#AES Decryption
dataforDecryption = Convert.makeListFromString(EncryptedData)
DecryptedMsg = aes.decryptData(dataforDecryption)

if len ( public_key ) <= 1 or len ( input_signature ) <= 1:
    print ( "Incorrect Inputs...!" )
    exit ()
else:
    #Signature Validation
    if (verify_signature ( public_key , DecryptedMsg.encode ( "UTF-8" ) , input_signature )):
    # print("Signature Verified..!")
        print ( "Decrypted Data : " , DecryptedMsg )
    else:
        print ( 'OOps..! Something Went Wrong..!' )
