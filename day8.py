import random

#function encrypt
def encrypt(word_encrypt):
    for i in range(size_word):
        letter = word[i]
        position = char.find(letter)
        new_word.append(char[position + number])

#function desencrypt
def desencrypt(word_encrypt):
    for i in range(size_word):
        letter = word[i]
        position = char.find(letter)
        new_word.append(char[position - number])

#char to list the alfabet
char = str('abcdefghijlmnopqrsituvxzabcdefghijlmnopqrsituvxzabcdefghijlmnopqrsituvxzabcdefghijlmnopqrsituvxzabcdefghijlmnopqrsituvxz')

#var to repeat or not the code
conti_or_no = 1
while conti_or_no == 1:
    enc_or_desenc = int(input("Do you want encrypt(0) or desencrypt(1) a word?"))
    if enc_or_desenc == 0:
        word = input("Type the word : ").lower()
        word_list = []
        new_word = []
        size_word = len(word)
        number = int(input("Type the number encryptor : "))

        for i in range(size_word):
            word_list.append(word[i])

        encrypt(word_list)
        encrypt_word = "".join(new_word)
        print(encrypt_word)
        conti_or_no = int(input("Do you wanna run again? 1 for Yes or 2 for No "))

    if enc_or_desenc == 1:
        word = input("Type the word : ")
        word_list = []
        new_word = []
        size_word = len(word)
        number = int(input("Type the number desencryptor : "))

        for i in range(size_word):
            word_list.append(word[i])

        desencrypt(word_list)
        desencrypt_word = "".join(new_word)
        print(desencrypt_word)
        conti_or_no = int(input("Do you wanna run again? 1 for Yes or 2 for No"))
