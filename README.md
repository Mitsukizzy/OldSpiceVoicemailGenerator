# Old Spice Voicemail Generator

### Execution Instructions
##### Requirements: Python 2.7+ and an Internet connection
First, download the oldspice.py file from this repository.

Windows: Open oldspice.py using the installed Python program

##### The following instructions will only work if you have Python installed on these respective terminals.
Cygwin: Type in "py oldspice.py" to run

Terminal: Type in "python oldspice.py" or "./oldspice.py" to run

### How it works
1. Using an online library of Old Spice voice chunks, I created a dictionary to map each choice to a sound filename.
2. The program prompts the user for gender, phone number, reason they can't come to the phone, and a fun ending.
3. A summary is printed and the user is asked for confirmation to create the voicemail.
4. The user must then name their new voicemail message.
5. Once all that information has been gathered, the program uses the choices from step 2 and downloads all the corresponding voice chunks using the entries in the dictionary.
6. The program determines the computer OS (since joining files has different commands in windows vs linus or max) and uses a terminal command to combine the chunks into one .mp3 file with the name requested in step 4.
