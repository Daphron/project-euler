import Queue
import sys
import math

def p18():
    sTriangle = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    sTriangle = sTriangle.split()

    triangle = Node(sTriangle[0])
    totalCount = 1
    queue = Queue.Queue()
    queue.put(triangle)
    #TODO: turn the string into a tree! while{for{}} structure maybe? 


    print "Done?"
    triangle.maximize()
    print triangle.getMax()

    queue = Queue.Queue()
    queue.put(triangle)
    while not queue.empty():
        tmp = queue.get()
        if tmp != None:
            sys.stdout.write(tmp.getValue())
            sys.stdout.write(' ')
            queue.put(tmp.getLeft())
            queue.put(tmp.getRight())
    


def testTree():
    n1 = Node(10)
    n2 = Node(100)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    n6 = Node(90)
    n7 = Node(70)
    n1.setLeft(n2)
    n1.setRight(n3)
    n2.setLeft(n4)
    n2.setRight(n5)
    n3.setLeft(n6)
    n3.setRight(n7)
    n1.maximize()
    print n1.getMax()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.max = value

    def setLeft(self, left):
        if self.left != None:
            print "ERROR HERE LEFT"
        self.left = left

    def setRight(self, right):
        self.right = right

    def maximize(self):
        if self.left != None and self.right != None:
            self.left.maximize()
            self.right.maximize()
            self.max = self.value +  max(self.left.getMax(), self.right.getMax())

    def getMax(self):
        return self.max

    def getValue(self):
        return self.value
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

if __name__ == "__main__":
    p18()
    #testTree()

