import AES
import Convert

#Input for AES Encryption
msg = input("Enter The Text to be Encrypted : ")
key = int(input("Enter Your Key : "))

#AES Object Generation
aes = AES.AES(key)

#Encryption
dataEncrypted = aes.encryptData(msg)
#print("This is the encrypted data:", dataEncrypted)

data = Convert.makeSingleString(dataEncrypted)
print("This is the encrypted data :", data)