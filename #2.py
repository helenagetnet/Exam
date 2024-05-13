#2
def create():
    stack = []
    return stack 
def isEmpty (stack):
    return len(stack) == 0
def push( stack , item):
    stack.append(item)
    print ('pushed item:' , item )
def pop (stack):
    if (isEmpty(stack)):
        return 'stack is empty'
    return stack.pop()
stack = create()
push (stack , str(1))
push (stack , str(2))
push (stack , str(3))
print ('stack after popping an element:' , str(stack))
print(stack)
