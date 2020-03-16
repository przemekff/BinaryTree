class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert_left(self, data):
        self.left = Node(data)

    def insert_right(self, data):
        self.right = Node(data)


class Calculator:

    avg = 0
    sum = 0
    counter = 0
    med = 0
    values = []

    def calc(self, node):
        if node == None:
            self.avg = self.sum/self.counter
            self.values.sort()
            length = len(self.values)
            if length%2 == 0:
                self.med = (self.values[(length//2)-1]
                 + self.values[length//2])/2
            else:
                self.med = self.values[length//2]
            return 
        self.sum += node.data
        self.counter +=1
        self.values.append(node.data)
        self.calc(node.left)
        self.calc(node.right)

    def reset(self):
        self.counter = 0
        self.sum = 0
        self.med = 0
        self.values = []
        self.avg = 0

    def output(self, node):
        print("For the chosen node the calculated values are as follows")
        print("Sum: ",self.sum)
        print("Average: ",self.avg)
        print("Median: ",self.med)



    





