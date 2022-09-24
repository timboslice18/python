#open, print and close file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)



#Write to file
#You can use mode = "a" to append instead of just "w" which overwrites it
#this also will create a new file if the file doesn't exist
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text.")