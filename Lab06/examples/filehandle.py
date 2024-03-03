# File Handling
f = open("haha.txt")

f = open("haha.txt", "rt")

# Read Files
f = open("haha.txt", "r")
print(f.read())

f = open("/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt", "r")
print(f.read())

f = open("haha.txt", "r")
print(f.read(5))

f = open("haha.txt", "r")
print(f.readline())

f = open("haha.txt", "r")
print(f.readline())

f = open("haha.txt", "r")
for x in f:
  print(x)

f = open("haha.txt", "r")
print(f.readline())
f.close()

# Write/Create Files
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

f = open("myfile.txt", "x")

f = open("myfile.txt", "w")

# Delete Files
import os
os.remove("haha.txt")

import os
if os.path.exists("haha.txt"):
  os.remove("haha.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")