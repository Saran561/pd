name = input('Ievadi savu vardu:')
print('Sveiks', name)
list_lohi = []

for i in range (5):
    momo = input('Ievadi random ciparu:')
    list_lohi.append(int(momo))
    


print(list_lohi)

print(sorted(list_lohi))
average = sum(list_lohi) / len(list_lohi)
print(average)