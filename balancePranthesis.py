from stack import Stack
from stack import Node

obj = Stack()

expression = input("Enter any expression :")


def balanced_parentheses(expression):
    open_List = "({["
    close_List = ")}]"

    for parabrk in expression:
        if parabrk in open_List:
            bracts = Node(parabrk)
            obj.push(bracts)
        elif parabrk in close_List:
            obj.pop()

    if obj.is_empty():
        print("Given expression is balanced!!")
    else:
        print("Given expression is Not balanced!!")


balanced_parentheses(expression)