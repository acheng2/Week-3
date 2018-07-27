class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.xlist = []
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.xlist.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        pop = self.xlist[0]
        self.xlist = self.xlist[1:]
        return pop

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        pop = self.xlist[0]
        return pop

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.xlist) == 0:
            return True
        else:
            return False
obj = MyQueue()
xlist = []
amount = int(input("How many numbers so you want to enter?"))
while amount > 0:
    x = int(input("what number would you like to queue"))
    obj.push(x)
    amount = amount - 1
amount2 = int(input("How many numbers do you want to remove at a time?")) - 1
amount3 = amount2
while amount2 > 0:
    obj.pop()
    amount2 = amount2 - 1
obj.pop()
obj.peek()
obj.empty()
print(obj.xlist)
d = True
while d == True:
    yn = input("Add another number?")
    if yn == "y":
        x = int(input("what number would you like to queue"))
        obj.push(x)
        while amount3 > 0:
            obj.pop()
            amount3 = amount3 - 1
        obj.peek()
        obj.empty()
        print(obj.xlist)
    if yn == "n":
        print("Thank You!")
        break
