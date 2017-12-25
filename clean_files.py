from textblob import TextBlob
import os
from natsort import natsorted


def find_and_remove_invalid_characters(filename):
    # Find invalid characters
    file = open(filename, "r")
    bad_chars = []
    for line in file:
        for word in line:
            analysis = TextBlob(word)
            try:
                current_polarity = analysis.sentiment[0]
            except UnicodeDecodeError:
                if word not in bad_chars:
                    bad_chars.append(word)
    file.close()

    # Make a copy of the file without these invalid characters
    with open(filename, 'r') as infile, open(filename + " copy.txt", 'w') as outfile:
        data = infile.read()
        for char_ in bad_chars:
            data = data.replace(char_, "")
        outfile.write(data)
    infile.close()
    outfile.close()

# Retrieves, sorts, and returns
# all valid txt files in directory
def get_txt_files():
    files = []
    for fn in os.listdir("."):
        if os.path.isfile(fn):
            if str(fn).endswith(".txt"):
                files.append(fn)
    return natsorted(files)


def multiple_file_clean():
    for file_ in get_txt_files():
        fs = find_and_remove_invalid_characters(file_)

multiple_file_clean()
