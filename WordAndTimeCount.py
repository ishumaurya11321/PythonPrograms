name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
mail=list()
for line in handle:
    if line.startswith('From '):
        piece=line.split()
        temp=piece[1]
        mail.append(temp)
for key in mail:
    count[key]=count.get(key,0) + 1
   
mosttime = None
mostword = None
for k,v in count.items():
    if mostword == 'none' or v > mosttime:
        mostword=k
        mosttime=v

print(mostword,mosttime)       
    
