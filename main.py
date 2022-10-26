# ******************************
# Make your Code
# ******************************
ascending = input().split()
ascending = list(map(int, ascending))

single = int(input())
for i in range(len(ascending)):
    if single < ascending[i]:
        ascending.insert(i, single)
        break
 
if single > ascending[-1]:
    ascending.append(single)

print(ascending)
