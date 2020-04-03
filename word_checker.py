import sys

reference_dictionary = "liste_francais.txt"
reference_dictionary_encoding = "ISO-8859-1"

source_file = "FICHIERS/PA_decrypted.txt"
source_file_encoding = "ISO-8859-1"





def main(reference_dictionary_in,reference_dictionary_encoding_in,source_file_in,source_file_encoding_in):
    sum_occurences = 0
    reference_file = open(reference_dictionary_in, "r", encoding=reference_dictionary_encoding_in)
    compared_file = open(source_file_in, "r", encoding=source_file_encoding_in)

    #conversion into data
    data = compared_file.read()

    for line in reference_file:
        occurrences = data.count(line.upper())
        if occurrences:
            sum_occurences += occurrences
            print("the word "+str(line)+"is present "+str(occurrences)+" times")

    print("we found "+str(sum_occurences)+" french words in "+str(number_of_words(data))+" words in total" )
    print(str(statistics(sum_occurences,number_of_words(data)))+" % of words in this file ")

    reference_file.close()
    compared_file.close()


def statistics(nbr_words_found, nbr_words_present):
    return (nbr_words_found/nbr_words_present)*100

def number_of_words(data_in):
    words = data_in.split()
    return len(words)

if __name__ == '__main__':
    main(reference_dictionary_in=sys.argv[1],reference_dictionary_encoding_in=sys.argv[2],source_file_in=sys.argv[3],source_file_encoding_in=sys.argv[4])

