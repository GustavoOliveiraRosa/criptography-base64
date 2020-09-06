import base64
import os
import time

os.system("clear")

print("██╗  ██╗██╗███████╗ ██████╗ ██╗  ██╗ █████╗ ")
print("██║  ██║██║██╔════╝██╔═══██╗██║ ██╔╝██╔══██╗")
print("███████║██║███████╗██║   ██║█████╔╝ ███████║")
print("██╔══██║██║╚════██║██║   ██║██╔═██╗ ██╔══██║")
print("██║  ██║██║███████║╚██████╔╝██║  ██╗██║  ██║")
print("╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ - Encrypter/Decrypter")
print("\n\033[0;0m") 
print("\033[;1m\033[1;97mOFICIAL TEXT ENCRYPTER BASE64 - https://github.com/GustavoOliveiraRosa/criptography-base64 \033[0;0m")
print("\033[1;36m--------------------------------------------\n\033[0;0m")

time.sleep(5)

os.system("clear")

print("██╗  ██╗██╗███████╗ ██████╗ ██╗  ██╗ █████╗ ")
print("██║  ██║██║██╔════╝██╔═══██╗██║ ██╔╝██╔══██╗")
print("███████║██║███████╗██║   ██║█████╔╝ ███████║")
print("██╔══██║██║╚════██║██║   ██║██╔═██╗ ██╔══██║")
print("██║  ██║██║███████║╚██████╔╝██║  ██╗██║  ██║")
print("╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ - Encrypter/Decrypter")
print("\n\033[0;0m") 
print("\033[;1m\033[1;97m1- Codificar \033[0;0m")
print("\033[;1m\033[1;97m2- Decodificar \033[0;0m")
print("\033[1;36m--------------------------------------------\n\033[0;0m")
escolha = input("Escolha ==>")


if escolha == "1":
    text_encode = input("Texto para cifrar: ")
    encoded = base64.b64encode(text_encode.encode())
    print('Texto criptografado: ',encoded)

if escolha == "2":
    text_decoded = input("Texto para decifrar:")
    decoded = base64.b64decode(text_decoded.encode())
    print('Texto descriptografado: ',decoded)

