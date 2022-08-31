word=input("Enter a word: ")
reverse_word =""
for i in range(len(word)):
   c=word[i]
   reverse_word=c+reverse_word
    
if(word==reverse_word):
    print("Your word is pelindrome")
else:
    print("Your word is not pelindrome")