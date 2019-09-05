import re
import string
import os
import time

def menu():

    """This is the main menu"""

    #Set options
    option1 = " 1. Search File"
    option2 = "2. Search Directory"

    print(option1,"\n", option2)

    menu_choice = input("\n\nSelect Option: ")

    if menu_choice == "1":
        target_file = input("Enter the filename to search: ")

        #Check if the filename is valid
        if os.path.isfile(target_file):
            #If valid, search the file for seed words
            search_file(target_file)
            print("\nSearch complete.")

        else:
            print("\nFile not found, please check and try again.\n")
            menu()

    elif menu_choice == "2":
        target_path = input("\nEnter the folder path :")

        #Clean the formatting of the input path
        target_path = target_path.rstrip('\\')
        target_path = target_path.rstrip('"')

        #Check if the path is valid
        if os.path.exists(target_path):

            #If valid, open each file in the folder and search for seed words
            for subdir, dirs, files in os.walk(target_path):
                for file in files:

                    if not file.startswith('.'): #This prevents opening hidden folders on Mac OS
                        search_file(os.path.join(subdir, file))

            print("\nSearch complete.")

        else:
            print("\nPath not found, please check and try again.\n")
            menu()

    else:
        print("\nPlease select a valid option...\n")
        menu()


def search_file(target):

    """This opens a file and searches for potential recovery seeds"""

    print("\nSearching", target, "...")
    time.sleep(2)

    with open(target, "r") as f:

        # Find all words in the file and store in list in lowercase
        matchword = re.findall("[a-z]+", f.read().lower())

        # If the list isn't empty
        if matchword:
            # Add a word to the end of matchword to capture seed words at the end of the file
            matchword.append("END")
            # Create an empty list called results
            results = []
            # Iterate through each word in the list of words pulled from the file
            for word in matchword:
                # Check if the word is a seed word
                if word in words:
                    # Add to a results list
                    results.append(word)
                else:
                    # If the list contains less than 4 items, clear it
                    if len(results) < 4:
                        results.clear()
                    else:
                        if len(results) < 12:
                            print("\n*** Partial Match Found in ", target, ":\n")
                            print("   ".join(results))
                            results.clear()
                        elif len(results) == 12:
                            print("\n*** 12 Word Recovery Seed Found in ", target, ":\n")
                            print("   ".join(results))
                            results.clear()
                        elif len(results) < 24:
                            print("\n*** Partial Match Found in ", target, ":\n")
                            print("   ".join(results))
                            results.clear()
                        elif len(results) == 24:
                            print("\n*** 24 Word Recovery Seed Found in ", target, ":\n")
                            print("   ".join(results))
                            results.clear()


""" The next 7 lines take a BIP 39 word list from a text file and 
stores the words to a list named 'words' """
#Set the variable wordfile as the text file containing the BIP 39 dictionary
wordfile = "bip39_wordlist.txt"

#Open the specified word list file
with open(wordfile,"r") as f:
    #Read each line and strip out white space then store in list
    words = [x.strip().lower() for x in f.readlines()]


""" Start the program """

menu()












