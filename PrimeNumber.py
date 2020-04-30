def prime(num):
    count = 1
    for i in range(1, num):
        if num % i == 0:
            count += 1
        if count > 2:
            break

    if count == 2:
        return True
    return False


rows, cols = (11, 2)
arr = [[0 for i in range(cols)] for j in range(rows)]

count = 0
k = 0
for m in range(1000 + 1):
    if prime(m):
        count = count + 1

    if m % 100 == 0 and m != 0:
        arr[k][0] = m
        arr[k][1] = count
        count = 0
        k = k + 1

j = 0
while j < 2:
    for n in range(10):
        print(arr[n][j],end=" ")
    print()
    j = j + 1