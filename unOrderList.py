fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word = line.rstrip().split()
    for element in word:
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)

search = input("Enter the word :")


def binarySearch(word, lst, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if word == lst[mid]:
        return True
    elif word > lst[mid]:
        return binarySearch(word, lst, mid + 1, high)
    elif word < lst[mid]:
        return binarySearch(word, lst, low, mid - 1)


if binarySearch(search, lst, 0, len(lst)):
 lst.remove(search)
else:
 lst.append(search)


print(lst)

f = open(fname, 'w')
for ele in lst:
    f.write(ele + '\n')

f.close()