import os
from datetime import datetime

# This function creates the log.txt file;
# Then it writes the current date and time to this file.
# Additionally, it prints "Hello, World!" to the terminal to
# verify if the program is running correctly.
def create_archive():
    print("Hello, World!")
    file = "log.txt"
    now = datetime.now()

    # I use the 'with' block to ensure the file is properly closed
    # and saved by the operating system, even if an error occurs
    # during writing.
    # I use 'utf-8' encoding so that accented strings,
    # like "Olá", don't break if the log is read on a Linux system
    # in the future.
    # The 'a' (append) mode was chosen to add new records to the end
    # of the file, protecting the history of previous executions.
    with open(file, "a", encoding="utf-8") as archive:
        archive.write("\nHello, World!\n")
        archive.write("This is a text file created in Python.\n")
        archive.write(f'Today\'s date: {now.strftime("%d/%m/%Y")}\n')
        archive.write(f'Current time [HH:MM:SS] -> {now.strftime("%H:%M:%S")}\n')
        archive.write(f'Current time [AM/PM] -> {now.strftime("%I:%M %p")}\n')

# This function aims to delete the file,
# for occasional testing, avoiding the need to delete it manually.
def delete_archive():
    file = "log.txt"
    try:
        os.remove(file)
        print("File deleted successfully!")
    except FileNotFoundError:
        print("File not found.")

create_archive()
# delete_archive()
