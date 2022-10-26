# ******************************
# Make your Code
# ******************************
ascending = input("numbers in ascending order: ").split()
ascending = list(map(int, ascending))
#ascending.sort() 

single = int(input("single number: "))
for i in range(len(ascending)):
    if single < ascending[i]:
        ascending.insert(i, single)
        break

print(*ascending)