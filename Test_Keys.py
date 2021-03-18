import PublicKeyGeneration as pkg
import SharedKeyGeneration as skg

#Key Generation Sample 1
priv1, pub1 = pkg.PublicKeyGeneration(128,6)
print('Private Key for Alex : ', priv1)
print('Public Key for Alex  : ', pub1)

#Key Generation Sample 2
priv2, pub2 = pkg.PublicKeyGeneration(128,6)
print('\nPrivate Key for Bob : ', priv2)
print('Public Key for Bob  : ', pub2)

#Shared Key Generation
s1 = skg.SharedKeyGeneration(priv1,pub2,128)
s2 = skg.SharedKeyGeneration(priv2,pub1,128)

#Key Validation
if(s1==s2):
    print('\nSuccess..!')
    print('Your Shared Key is : ', s1)