# Trying to learn string manipulation
# Create a function for Caesar Cipher
# Decrypt the cipher
# work on Vigenere Cipher 
#Decrypt the vigenere cipher

myString = 'This is a string value'

# indexing strings
print(myString[12])
print(myString[-1])

# slicing through a string
print(myString[3:8])
print (myString[12:-1])

# using some string methods
print(myString.split())
print(myString.capitalize())
print(myString.upper())
print(myString.isalpha())
print(myString.isspace())
print(myString.find('r'))

# Add ons that I do not know how to describe
print(len(myString))
print(list(myString))


## Caesar Cipher 
## Caesar cipher takes the number equivalent of a letter and adds 3 to it to get encrypt it
def Caesar_Cipher():
    reference = 'abcdefghijklmnopqrstuvwxyz'
    method = input('Encrypt or Decrypt? Type E for encrypt and D for decrypt: ').upper()
    key = 3
    
    if method == 'D':
        word = input('Enter the message to be decrypted: ').lower()
        word_list = list(word)
        Final_message = ''
        for i in word_list:
            if not i.isalpha():
                Final_message += i
            else:
                index = reference.find(i)
                new_index = (index - 3)%26
                decrypted_letter = reference[new_index]
                Final_message += decrypted_letter
    elif method == 'E':
        word = input('Enter the message to be encrypted: ').lower()
        word_list = list(word)
        Final_message = ''
        for i in word_list:
            if not i.isalpha():
                Final_message += i
            else:
                index = reference.find(i)
                new_index = (index + 3)%26
                encrypted_letter = reference[new_index]
                Final_message += encrypted_letter
        
        
    return Final_message.capitalize()

print(Caesar_Cipher())


                
                 
    
     
