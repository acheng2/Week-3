class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.xlist = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.xlist.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.xlist) > 0:
            pop = self.xlist[len(self.xlist) - 1]
            self.xlist = self.xlist[0:(len(self.xlist) - 2)]
            return pop

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        pop = self.xlist[len(self.xlist) - 1]
        return pop

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.xlist) == 0:
            return True
        else:
            return False

obj = MyStack()
xlist = []
amount = int(input("How many numbers so you want to enter?"))
while amount > 0:
    x = int(input("what number would you like to queue"))
    obj.push(x)
    amount = amount - 1
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
obj.pop()
obj.top()
obj.empty()
print(obj.xlist)
