import rsa
import base64

#Generer public og private keys med det antal af bits man ønsker (Skal være mellem 16 og 1024)
publicKey, privateKey = rsa.newkeys(1024)

#Besked man gerne vil have krypteret
message = "Dette er en meget hemmelig besked"

#rsa kryptere beskeden med public key
encMessage = rsa.encrypt(message.encode(), publicKey)
#Den krypteret besked bliver krypteret igen med base64
base64Message = base64.b64encode(encMessage)

#Vis den originale besked
print("original besked:", message)
#Vis den krypteret besked
print("krypteret besked:", base64Message)

#Dekryptere beskeden med base64
decbase64Message = base64.b64decode(base64Message)
#Dekryptere den dekrypterede base64 besked med vores private key
decMessage = rsa.decrypt(encMessage, privateKey).decode()

#Viser den dekrypterede besked 
print("dekrypteret besked:", decMessage, "\n")
#Viser public key
print(publicKey, "\n")
#Viser private key
print(privateKey)

#for at køre koden installer 
#pip install rsa


