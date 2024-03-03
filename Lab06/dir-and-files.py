# Exercise 1
import os
def list_(path):
    d = []
    f = []
    all = []
    for entry in os.listdir(path):
        full = os.path.join(path, entry)
        if os.path.isdir(full):
            d.append(entry)
        elif os.path.isfile(full):
            f.append(entry)
        all.append(entry)
    return d, f, all

path = "/Users/akerkezhanykul/Desktop/pp2"
d, f, all = list_(path)
print("Directories:", d)
print("Files:", f)
print("All Directories and Files:", all)

# Exercise 2
import os
print('Exist:', os.access('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt', os.F_OK))
print('Readable:', os.access('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt', os.R_OK))
print('Writable:', os.access('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt', os.W_OK))
print('Executable:', os.access('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt', os.X_OK))

# Exercise 3
import os
path = r'/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt'
print("Puth exists:")
print(os.path.exists(path))

print("\nFile name:")
print(os.path.basename(path))

print("\nDirectorie:")
print(os.path.dirname(path))

# Exercise 4
with open(r"/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Number of lines in fail:', lines)

# Exercise 5
items = ['Morning ', 'Afternoon ', 'Evening ']
f = open('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt','w')
f.writelines(items)
f.close()

# Exercise 6
import string, os
if not os.path.exists("A-Z"):
   os.makedirs("A-Z")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

# Exercise 7
#1
import shutil 
shutil.copyfile('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt','/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/demofile2.txt')
#2
with open('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/haha.txt','r') as first, open('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/demofile2.txt','w') as second: 
	for line in first: 
			second.write(line)

# Exercise 8
import os
print('Readable:', os.access('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/demofiles2.txt', os.R_OK))
print('Writable:', os.access('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/demofile2.txt', os.W_OK))
print('Executable:', os.access('/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/demofile2.txt', os.X_OK))
if os.path.exists("/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/demofile2.txt"):
  os.remove("/Users/akerkezhanykul/Desktop/pp2/Lab06/examples/demofile2.txt")
else:
  print("The file does not exist")
