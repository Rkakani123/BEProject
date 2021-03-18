import AES
import Convert

#Input for AES Encryption
msg = input("Enter The Text To Be Decrypted : ")
key = int(input("Enter Your Shared Key : "))
#Converting single string into list
dataforDecryption = Convert.makeListFromString(msg)

#AES Object Generation
aes = AES.AES(key)

#AES Decryption
PlainText = aes.decryptData(dataforDecryption)
print("This is the decrypted data:", PlainText)