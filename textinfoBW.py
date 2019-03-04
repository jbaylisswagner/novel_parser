"""
Author: Bayliss Wagner
Date: 11/19
"""

import filemenu
from string import *
#functions provided by filemenu: filemenu.list_files & filemenu.menu_selection

def main():

    print()
    #allow user to choose corpus
    folder = 'texts'
    files = filemenu.list_files(folder)
    #get index of chosen book
    file1 = filemenu.menu_selection(files,
        "Enter choice for the 1st text: ")

    file2 = filemenu.menu_selection(files,
        "Enter choice for the 2nd text: ")

    #translate number of book from file menu into the name of the book as a str
    book1 = files[file1]
    book2 = files[file2]

    #pass corpus into functions in order to find word count
    #most frequent words
    bookstring = clean(book1)
    word_lst = bookstring.split()
    count_lst_1 = count_words(word_lst)
    top_freq(count_lst_1, book1)

    bookstring2 = clean(book2)
    word_lst2 = bookstring2.split()
    count_lst_2 = count_words(word_lst2)
    top_freq(count_lst_2, book2)

    n1 = len(word_lst) #number of words in book 1
    n2 = len(word_lst2) #number of words in book 2

    get_distinctiveness(count_lst_1, n1, book1, count_lst_2, n2, book2)

    #to find the context in both texts for the same word:
    query = input("\nWhich word would you like to see in context? ")

    while query != "":

        get_context(query, word_lst, book1)
        get_context(query, word_lst2, book2)

        query = input("Which word would you like to see in context? ")

def clean(filename):
    """
    Purpose: read a novel file and return a long string consisting only of
    words separated by spaces
    Parameter: filename, as a string (ex: "shelley_frankenstein.txt")
    Return: a string
    """
    # open the file in read mode in the data/cs21/novels folder

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
    search list of words in the novel for words in order to MUTATE LIST
    of the number of times at which each word appears
    mutate list: add one to count if word is found
    if not found, insert word and count of 1
    lst format: [["the", 7823], ["greatest", 24]
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
        lst.insert(low, [query, 1])

def count_words(word_lst):
    """
    Purpose: create list of lists of word and count, sorted by counts,
    then calculate most prevalent words
    Parameter: string (of all of the text in the novel, separated by spaces)
    Return list of words and their counts, sorted alphabetically by word
    """
    stop_words = {}
    count_lst = []
    user_input = input("Include stopwords? Reply 'yes' or 'no.' \n")

    if user_input == "no":
		stop_words = get_stopwords()

    for word in word_lst:
        #remove stopwords!!!
        if word not in stop_words:
            #create list of counts of each word in word list
            binary_search(word, count_lst)

    return count_lst

def get_stopwords():
    """Removes common words and articles from the analysis of word
    frequency.
    """
    stopwords = {}
    infile = open("stopwords.txt", 'r')
    for line in infile:
        word = line.strip()
        stopwords[word] = word
    return stopwords


def swap(i, j, lst):
        temp1 = lst[i]
        lst[i] = lst[j]
        lst[j] = temp1

def selection_sort(lst):
    """
    Purpose: sort list of word counts by frequency at which words occur instead
    of alphabetically
    Parameter: list of words, which will be modified by sorting
    """

    for i in range(len(lst)):
        m = i
        for j in range(i, len(lst)):
            if lst[j][1] < lst[m][1]:
                m = j
        swap(i, m, lst)


def top_freq(lst, bookname):

    #create new list that is a copy of the counts list
    freq_lst = lst[:]
    #sort this list by frequency of word occurrences instead of alphabetically
    selection_sort(freq_lst)

    print("\nThe top 10 most frequent words in %s are:\n" % (bookname))

    print("Frequency | Word ")
    print("----------|------------------------")

    for i in range(10):
        index = len(freq_lst) - 1 - i #count backwards to begin
        #with most frequent word
        freq = freq_lst[index][1]
        word = freq_lst[index][0]
        print("%-9d | %s" %(freq, word))

def distinct_search(query, lst2, distinct_lst1, distinct_lst2, n1, n2, count1):
    """
    search list of words in the novel for words in order to MUTATE LIST
    of the number of times at which each word appears
    mutate list: add one to count if word is found
    if not found, insert word and count of 1
    lst format: [["the", 60.7], ["greatest", 90.3]
    parameters: lists of words and their frequencies
    """
    low = 0
    high = len(lst2) - 1 #INITIALIZE AT ZERO BC LIST IS EMPTY

    while low <= high:
        mid = int((high + low)/2) #int rounds down

        if query == lst2[mid][0]:
            #if the word is in both texts, calculate distinctiveness score
            count2 = lst2[mid][1]
            score = ((count1/n1)/(count2/n2))
            distinct_lst1.append([query, score])
            #compute inverse of each score for book 2 relative to book 1
            inverse = 1/score
            distinct_lst2.append([query, inverse])
            return #exit function

        elif query > lst2[mid][0]:
            low = mid + 1

        elif query < lst2[mid][0]:
            high = mid - 1

def get_distinctiveness(lst1, n1, bookname1, lst2, n2, bookname2):
    """
    Purpose: count how often each word occurs relative to the number of words
    in each text. display distinctiveness scores in table.
    Parameters:
    lst1 and lst2 are the lists of words and their counts, sorted alphabetically
    bookname1 and bookname2 are strings
    n1 and n2 are lists of the amount of words in each book
    """

    distinct_lst1 = [] #list of words and their distinctiveness scores
    #for book 1 relative to book 2
    distinct_lst2 = [] #list of distinctiveness scores
    #for book 2 relative to book 1

    #build up both distinctiveness lists, starting with 1 relative to 2
    for i in range(len(lst1)): #goes through each ["word", count integer]
        word = lst1[i][0]
        word_freq = lst1[i][1]
        distinct_search(word, lst2, distinct_lst1, distinct_lst2,
            n1, n2, word_freq)

    print("\nThe top 10 most prevalent words in %s \n relative to %s are: \n"
            %(bookname1, bookname2))

    print(" Score    | Word ")
    print("----------|------------------------")

    selection_sort(distinct_lst1) #sort so that highest distinctiveness
    #scores are at the end of the list

    for i in range(10):
        index = len(distinct_lst1) - 1 - i #count backwards to begin
        #with most distinct word
        distinct_score = distinct_lst1[index][1]
        word = distinct_lst1[index][0]
        print("%-9.1f | %s" %(distinct_score, word))

    print("\nThe top 10 most prevalent words in %s \n relative to %s are: \n"
            %(bookname2, bookname1))

    print(" Score    | Word ")
    print("----------|------------------------")

    selection_sort(distinct_lst2)

    for i in range(10):
        index = len(distinct_lst2) - 1 - i
        distinct_score = distinct_lst2[index][1]
        word = distinct_lst2[index][0]
        print("%-9.1f | %s" %(distinct_score, word))


def get_context(query, word_lst, novel_name):
    """
    Purpose: display the words surrounding the word that the user enters
    at each instance in which it appears in the text
    *make sure program can handle a word that doesn't exist in the text*
    Parameter: list of words in the novel
    """

    print("\n Here are the occurrences of %s in %s:" %(query, novel_name))
    print("-"*40)
    print()

    #find all indices at which the query occurs
    location_lst = linear_search(query, word_lst)

    if len(location_lst) == 0:
        print("The word you entered is not in this text.\n")

    else:
        for location in location_lst:
            forewords = " ".join(word_lst[(location-4):location])
            postwords = " ".join(word_lst[(location+1):(location+5)])
            print("%25s %s %-75s" %(forewords, query, postwords))

    print("-"*40)
    print()

main()
