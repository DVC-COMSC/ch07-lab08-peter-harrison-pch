# ******************************
# Make your Code
# ******************************
ascending = input().split()
ascending = list(map(int, ascending))
#ascending.sort() 

single = int(input())
for i in range(len(ascending)):
    if single < ascending[i]:
        ascending.insert(i, single)
        break

print(*ascending)