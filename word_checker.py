reference_dictionary = "liste_francais.txt"
reference_dictionary_encoding = "ISO-8859-1"

source_file = "FICHIERS/PA_decrypted.txt"
source_file_encoding = "ISO-8859-1"





def main():
    sum_occurences = 0
    reference_file = open(reference_dictionary, "r", encoding=reference_dictionary_encoding)
    compared_file = open(source_file, "r", encoding=source_file_encoding)

    #conversion into data
    data = compared_file.read()

    for line in reference_file:
        occurrences = data.count(line.upper())
        if occurrences:
            sum_occurences += occurrences
            print("the word "+str(line)+"is present "+str(occurrences)+" times")


    print(statistics(sum_occurences,number_of_words(data)))
    print(sum_occurences)
    reference_file.close()
    compared_file.close()


def statistics(nbr_words_found, nbr_words_present):
    return (nbr_words_found/nbr_words_present)*100

def number_of_words(data_in):
    words = data_in.split()
    return len(words)

if __name__ == '__main__':
    main()

