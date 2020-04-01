import string

#print(list(string.ascii_lowercase[1]))


f=open("dictionnary_generated.txt", "a+")

def writeFile(text):
    f.write(text+"\n")

def word_generator(number_of_letter):
    word_list_temp=[]

    for id_column in range(0,number_of_letter):
        print("id_column"+str(id_column))
        word_list_temp.insert(id_column, string.ascii_lowercase[id_letter])
        for id_letter in range(0, 26):
            var_letter = string.ascii_lowercase[id_letter]
            #word_list_temp.insert(id_column, string.ascii_lowercase[id_letter])
            #word_list_temp[id_column]=string.ascii_lowercase[id_letter]
            print(word_list_temp)


#word_generator(2)

number=1000
for x in range(0,number):
    #print(x)
    liste=["1","2","3"]
#    print(len(str(x)))
    liste[len(str(x))]=string.ascii_lowercase[1]
    liste[1] = string.ascii_lowercase[list(str(x)[1])]
    #print(liste)
