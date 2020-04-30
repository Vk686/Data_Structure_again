name = input("Enter file name: ")
fh = open(name)
lst = list()
for line in fh:
    word = line.rstrip().split()
    for element in word:
        if element in lst:
            continue
        else:
            lst.append(element)

test_list = [int(i) for i in lst]
test_list.sort()
# Printing modified list
print("Modified list is : " + str(test_list))


search = int(input("Enter the Value :"))


def binarySearch(value, test_list, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if value == test_list[mid]:
        return True
    elif value > test_list[mid]:
        return binarySearch(value, test_list, mid + 1, high)
    elif value < test_list[mid]:
        return binarySearch(value, test_list, low, mid - 1)


if binarySearch(search, test_list, 0, len(test_list)):
    test_list.remove(search)
else:
    test_list.append(search)

test_list.sort()
print(test_list)