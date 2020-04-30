from queue import Queue

from stack import Node

from PrimeNumber import prime


obj = Queue()

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

# finding the length of prime anagram list
length = len(prime_anagram)

# Adding the prime anagram in to queue
for number in range(length):
    num = Node(prime_anagram[number])
    obj.enqueqe(num)

# Printend the anagram from queue
obj.traverse()