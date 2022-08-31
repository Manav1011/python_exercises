import re
import os
class ceaser_cipher:
    ciphertext=""
    def __init__(self,plaintext):
        self.plaintext = plaintext
    def encrypt(self):
        for i in list(self.plaintext):
            if re.search("[a-wA-W]",i):
                ceaser_cipher.ciphertext = ceaser_cipher.ciphertext+chr(ord(i)+3)
            elif re.search("[x-zX-Z]",i):
                ceaser_cipher.ciphertext = ceaser_cipher.ciphertext+chr((ord(i)-26)+3)
        print(f"Your cipher text is {ceaser_cipher.ciphertext}")
    def decrypt(self):
        self.plaintext =""
        for i in list(ceaser_cipher.ciphertext):
            if re.search("[d-zD-Z]",i):
                self.plaintext = self.plaintext+chr(ord(i)-3)
            elif re.search("[a-cA-c]",i):
                self.plaintext = self.plaintext+chr((ord(i)+26)-3)
        print(f"Your plain text is {self.plaintext}")
os.system("cls")
user=ceaser_cipher(input("Enter your plain text: "))
user.encrypt()
com=input("Do you want to apply decreption to this ciphertext[y/n]: ")
if not re.search("y|n",com):
    print("Please enter a correct choice")
else:
    if com=="y":
        user.decrypt()
    else:
        pass

        
        