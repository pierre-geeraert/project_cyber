import string

#print(list(string.ascii_lowercase[1]))


f=open("dictionnary_generated.txt", "a+")

def writeFile(text):
    f.write(text+"\n")

def word_generator(number_of_letter):
    word_list_temp=[""]*number_of_letter

    for id_column in range(0,number_of_letter):
        print("id_column"+str(id_column))
        for id_letter_2 in range(0,26):
            word_list_temp[(number_of_letter-1)-id_column]=string.ascii_lowercase[id_letter_2]
            for id_letter in range(0, 26):
                word_list_temp[(number_of_letter-1)]=string.ascii_lowercase[id_letter]
                print(word_list_temp)
                writeFile(str(word_list_temp))


word_generator(3)


