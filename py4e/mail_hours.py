name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = 0
dic = {}
for line in handle:
    if not line.startswith("From "):
        continue
    aux = int(line.split()[5][:2])
    dic[aux] = dic.get(aux, 0) + 1
    
ls = []
for k,v in dic.items():
    ls.append((k,v))

ls.sort()
for k,v in ls:
    print(str(k).rjust(2,'0'), str(v))
