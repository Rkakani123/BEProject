import AES
import Convert
from ECDSA import *
from ImageEncryption import *

#inputs
msg = input("Enter The Text to be Encrypted : ")
private_key = int(input("Enter Your Shared Key : "))

#AES Object Generation
aes = AES.AES(private_key)
#AES Encryption
dataEncrypted = aes.encryptData(msg)
data = Convert.makeSingleString(dataEncrypted)

#Public Key Generation
public_key = scalar_mult(private_key, curve.g)
#print(public_key)

#Signature Generation
signature = sign_message(private_key, msg.encode('UTF-8'))

#Finally Cipher Generation
#cipher = "P:"+str(signature[0])+":Q:"+str(signature[1])+":Data:"+data
cipher = Convert.DictToString(signature,data)
print(cipher)
'''
cipher ={
        "Signature": signature,
        "Data": data,
        }
print(cipher)
'''

#Input Cover Image
input_file = input("Enter Cover Image Name : ")
#data = input("Enter Your Secret Data : ")

#Putting Cipher inside Cover Image
if(imageEncrypt(input_file,cipher)):
    print("Operation Successfully Completed...!")
else:
    print("Something Went Wrong..!")
