# Imports the argv module from system
from sys import argv
#takes two arguments and stores in argv
script, filename = argv
# opens the given file and stores it in text 
txt = open(filename)
# ask for filename
print(f"here is your {filename}: ")
# Uses the read function to read the file and outputs on standard output
print(txt.read()) 


txt_input = input("Enter your file name:")
read_txt_input = open(txt_input)
print(read_txt_input.read())

txt.close()
read_txt_input.close()
