fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        piece = line.split()
        print(piece[1])
        count=count + 1
print("There were", count, "lines in the file with From as the first word")
