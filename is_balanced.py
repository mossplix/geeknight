def is_balanced(expr):
    left = "({["
    right = ")}]"
    stack = Stack()
    for e in expr:
        if e in left:
            stack.push(e)
        elif e in right:
            if stack.is_empty():
                return False
            if right.index(e) != left.index(stack.pop()):
                return False

    return stack.is_empty()