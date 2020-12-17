fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    aux = line.rstrip().split()
    for w in aux:
        if w not in lst:
            lst.append(w)
    lst.sort()

print(lst)
