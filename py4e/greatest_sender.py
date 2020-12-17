name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = {}
for line in handle:
    if not "From " in line:
        continue
    email = line.split()[1]
    dic[email] = dic.get(email, 0) + 1

greatest = None
email = None
for k,v in dic.items():
    if greatest == None or v > greatest:
        greatest = v
        email = k

print(email, greatest)
