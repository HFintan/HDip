# Problem 9
# Reads a file, outputs every second line.

# Lifted pretty much verbatim from
# https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po
# with sys from
# https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python
# Not a whole lot of original thought in this script,
# I'm afraid, but things keep cropping up which demand
# my time...

import sys

with open(sys.argv[1],"r") as file_to_read:
    for count, line in enumerate(file_to_read, start =1):
        if count % 2 == 0:
            print(line)
