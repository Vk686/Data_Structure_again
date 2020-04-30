from PrimeNumber import prime
from stack import Stack
from stack import Node


obj = Stack()

prime_obj = prime()

prime_anagram = []

prime_list = prime_obj.prime(0, 1000)


for num in prime_list:
    if num <= 10:
        continue
    number = prime_obj.anagram(num)
    if prime_obj.prime_check(number) and 0 <= number <= 1000:
        prime_anagram.append(number)
        prime_anagram.append(num)
        prime_list.remove(number)

length = len(prime_anagram)


for number in range(length):
    num = Node(prime_anagram[number])
    obj.push(num)

for number in range(length):
    data = obj.pop()
    print(data, end=" ")