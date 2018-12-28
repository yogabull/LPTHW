from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file ...")

"""Here are notes on the OPEN fuction argument modes:

The OPEN function has argument modes.
r   Open text file for reading. Stream positioned at file's beginning.
r+  Open for reading and writing. Stream position file beginning..
w   Truncate file to zero length or create file for writing.  Stream beginning..
w+  Open for reading and writing. File created if it doesn't exist.
    Otherwise it is truncated. Stream position file beginning.
a   Open for writing. File created if it doesn't exist.
    Stream positioned at end of file.
a+  Open for reading/writing. Create file if it doesn't exist.
    Subsequent writes end at the then current end of file.

"""

#The 'w' allows for the file to be overwritten.
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you a for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# This line shoud concatonate the previous lines:
nl = '\n' #just seeing this work.
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

print("And finally, we close it.")
target.close()
