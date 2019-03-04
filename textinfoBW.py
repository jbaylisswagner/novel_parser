def main():

    print()
    bookfile = input("Enter the book's filename: ")
    bookstring = clean(bookfile)
    word_lst = bookstring.split()
    count_words(word_lst)

    get_context(word_lst)


def clean(filename):
    """
    Purpose: read a novel file and return a long string consisting only of
    words separated by spaces
    Parameter: filename, as a string (ex: "shelley_frankenstein.txt")
    Return: a string
    """
    # open the file in read mode in the data/cs21/novels folder

    #filename = "/data/cs21/novels/" + filename
    word_file = open(filename,'r')
    bookstring = "" # set up string accumulator

    # loop through each line (one word on each line)
    for line in word_file:
        line = line.lower() #make lowercase
        for char in line:
            if char.isalpha():
                bookstring = bookstring + char
            else: #turn special characters into spaces
                bookstring = bookstring + " "

    word_file.close()
    return bookstring

def linear_search(query, lst):

    list_of_indices = []

    for i in range(len(lst)):
        if query == lst[i]:
            list_of_indices.append(i)

    return list_of_indices

def binary_search(query, lst):
    """
    search count list for words
    mutate list: add one to count if word is found
    if not found, insert word and count of 1
    """
    low = 0
    high = len(lst) - 1 #INITIALIZE AT ZERO BC LIST IS EMPTY

    while low <= high:
        mid = int((high + low)/2) #int rounds down

        if query == lst[mid][0]:
            lst[mid][1] += 1 #if the word matches, increase count
            #inside the count list
            return #exit function

        elif query > lst[mid][0]:
            low = mid + 1

        elif query < lst[mid][0]:
            high = mid - 1

    if low > high: #binary search stops here
        #differentiate from mid?
        lst.insert(low, [query, 1])

def count_words(word_lst):
    """
    Purpose: create list of lists of word and count, sorted by counts,
    then calculate and print the most common word
    Parameter: string (of all of the text in the novel, separated by spaces)
    """

    count_lst = []

    for word in word_lst:
        #create list of counts of each word in word list
        binary_search(word, count_lst)

    #find maximum of count, find index
    maximum = count_lst[0][1]

    for i in range(1, len(count_lst)):

        if count_lst[i][1] > maximum:
            maximum = count_lst[i][1]
            max_index = i

    commonword = count_lst[max_index][0]
    print("\nThe most common word is '%s,' which occurs %d times.\n"
     %(commonword, maximum))



def get_context(word_lst):
    """
    Purpose: display the words surrounding a word that the user enters
    at each instance in which it appears in the text
    *make sure program can handle a word that doesn't exist in the text*
    Parameter: list of words in the novel
    """

    query = input("Which word would you like to see in context? ")

    while query in word_lst and query != "":

        #find all indices at which the query occurs
        location_lst = linear_search(query, word_lst)

        if len(location_lst) == 0:
            print("The word you entered is not in this text.\n")

        else:
            for location in location_lst:
                forewords = " ".join(word_lst[(location-4):location])
                postwords = " ".join(word_lst[(location+1):(location+5)])
                print("%25s %s %-75s" %(forewords, query, postwords))

        query = input("Which word would you like to see in context? ")

main()
