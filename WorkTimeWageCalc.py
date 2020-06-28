name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
hour=list()
for line in handle:
    if line.startswith('From '):
        piece=line.split()
        temp=piece[5]
        hour.append(temp)
xi=list()        
for i in hour:
    x=i.split(':')
    xi.append(x[0])
    
        
    
for key in xi:
    count[key]=count.get(key,0) + 1
    
lst=list()
for k,v in count.items():
    tlst=(k, v)
    lst.append(tlst)
    
solved=sorted(lst)
for k,v in solved:
    print(k, v)
    