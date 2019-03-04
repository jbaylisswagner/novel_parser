from os.path import isfile
from os import listdir

#This file was written by the Swarthmore CS Department.

def list_files(folder):
    """ Given a folder/directory name, enumerate the .txt files
    in the directory and return the names in a list. """
    print("Here are the files in the text folder:")
    txt_files = []
    all_files = sorted(listdir(folder))
    for i in range(len(all_files)):
        file = all_files[i]
        if file.endswith('.txt'):
            print('[%2d] %s' % (i, file))
            txt_files.append('%s/%s' % (folder, file))
    print()
    return txt_files

def menu_selection(choices, prompt):
    """ Present the user with a prompt asking for a choice from a
    list of choices verify that the selection is correct. Expects
    a numerical input.
    """
    valid = False
    while not valid:
        choice = input(prompt)
        if not choice.isdigit():
            print("Only integers are accepted, try again.")
        else:
            choice = int(choice)
            if choice < 0 or choice >= len(choices):
                print("That selection is out of range, try again.")
            else:
                valid = True

    return choice

def main():
    folder = '/texts'
    files = list_files(folder)
    selection = menu_selection(files, "Enter choice for the 1st text: ")
    print("Your selection: %s" % (files[selection]))

if __name__=='__main__':
    main()
