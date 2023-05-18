from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")

print("iF you do not wish to continue press ctrl-c.")
print("press enter if you wish to continue.")

input(" ? ")
print("opening the file ...")
target = open(filename, 'w')
print("Truncating the file! Goodbye")
target.truncate()
print("Now I am going to ask you to write three lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")
print("Writing the three lines to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target = open(filename)

print(target.read())

print("Erasing the file now ...")

target = open(filename,'r+')

target.truncate()

target.close()

