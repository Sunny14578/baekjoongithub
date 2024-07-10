n = input()
l = []
for i in n:
    l.append(int(i))
l.sort(reverse=True)
print("".join(map(str, l)))