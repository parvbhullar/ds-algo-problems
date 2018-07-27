def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    d = 1
    gcd = d
    while d <= num:
        i = 0
        passed = True
        while i < len(arr):
            _gcd(arr[i], gcd)
            i += 1

        if passed and d > gcd:
            gcd = d

        d += 1

    return gcd

def _gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# GCD of more than two (or array) numbers

# Function implements the Euclidian
# algorithm to find H.C.F. of two number
def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


import math

import math


def ClosestXdestinations(numDestinations, allLocations, numDeliveries):
    # WRITE YOUR CODE HERE
    current_location = 0

    i = 0
    # size = len(allLocations)
    dist_arr = []
    dict = {}
    while (i < numDestinations):
        dist = calc_distance(allLocations[i][0], allLocations[i][1])
        dist_arr.append(dist)
        dict[dist] = allLocations[i]
        i += 1

    # print dist_arr
    dist_arr.sort()
    # print dist_arr

    j = 0
    result = []
    while j < numDeliveries:
        if dist_arr[j] in dict:
            result.append(dict[dist_arr[j]])
        j += 1

    return result


def calc_distance(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


# ClosestXdestinations(3, [[1,2], [3,4], [1, -1]], 2)

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self,val):
        return self.stack.append(val)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

# P1. Implement a queue

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.insert(0,val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

class QueueWithStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,el):
        self.stack1.push(el)

    def dequeue(self):
        if not self.stack2.size > 0:
            self.move_content()
        return self.stack2.pop()

    def move_content(self):
        while self.stack1.size > 0:
            self.stack2.push(self.stack1.pop())

def is_balanced(brackets):
    open_brackets = ["(","{","["]
    close_brackets = [")","}","]"]
    bracket_matches = {")":"(", "}":"{", "]":"["}
    stack = Stack()

    # loop through each brackets
    for bracket in brackets:
        # if open,
        if bracket in open_brackets:
            # store in stack
            stack.push(bracket)
        # if closed,
        else:
            # check if the top of the stack is the open bracket of the same type
            if bracket_matches[bracket] == stack.peak():
                # remove the pair
                stack.pop()
            # otherwise,
            else:
                # invalid string
                return False

    # after looping through, valid if the stack is empty
    # invalid otherwise
    return not stack.size()

def sort_stack(stack):
    result = Stack()
    while stack.size() > 0:
        # pop the top el from stack
        el = stack.pop()
        # until the top el is smaller than el
        num_popped_from_result = 0
        while result.peak() > el:
            # pop els from result and push them to stack
            stack.push(result.pop())
            num_popped_from_result += 1
        # push el
        result.push(el)
        # push els popped back to result
        for i in range(num_popped_from_result):
            result.push(stack.pop())
    return result

# if __name__ == "__main__":
#     stack = Stack()
#     stack.push(4)
#     stack.push(5)
#     stack.push(2)
#     stack.push(1)
#     stack = sort_stack(stack)
#     print stack.stack

# if __name__ == "__main__":
# print is_balanced("{[()]}")
# print is_balanced("{[(])}")
# print is_balanced("{{[[(())]]}}")

class LN_Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

    def traverse(self):
        node = self
        while node != None:
            print node.val
            node = node.next


class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value



from collections import defaultdict

class Graph:
    start = [0, 0]
    current = start
    last = start
    graph = defaultdict(defaultdict(list))
    # def __init__(self):

    def addEdge(self, row, col, val):
        self.graph[row][col].append(val)



class FindPath:
    row_nums = 0
    col_nums = 0
    visited = []

    def minimumDistanceDFS(self, numRows, numColumns, area):
        # WRITE YOUR CODE HERE
        self.row_nums = numRows
        self.col_nums = numColumns

        row = 0
        col = 0
        paths = [[0]]
        # self.visited = area
        # Mark all the vertices as not visited
        self.visited = [0] * (len(self.area))

        return self.countPaths(area, row, col, paths)

    def countPaths(self, area, row, col, paths):
        self.visited[row][col] = 2

        right = [row, col + 1]
        left = [row, col - 1]
        top = [row - 1, col]
        down = [row + 1, col]

        check_nbr = [down, right, top, left]
        result = 0

        i = 0
        while i < len(check_nbr):
            # isSafe and value check for left, top, right, down
            v = self.isVisited(check_nbr[i])
            valid = self.isValid(check_nbr[i])
            x_row = check_nbr[i][0]
            y_col = check_nbr[i][1]
            if v:
                print 'visited - ' + str(check_nbr[i])
            elif valid is False:
                print 'invalid - ' + str(check_nbr[i])
            elif self.isAtDest(check_nbr[i], area):
                print 'dest at - ' + str(check_nbr[i]) + ' - ' + str(result)
                return 1
            elif self.isPath(check_nbr[i], area):
                print 'path exists - ' + str(check_nbr[i])
                # result += 1
                result += self.countPaths(area, x_row, y_col, paths)
            else:
                print 'path not exists - ' + str(check_nbr[i])

            # if v is False and valid:
            #     self.visited[x_row][y_col] = 2

            i += 1


        return result
        # return paths[row][col]

    def isVisited(self, cell):
        x_row = cell[0]
        y_col = cell[1]
        try:
            if self.visited[x_row][y_col] == 2:
                return True
        except IndexError:
            print 'sorry, no found' + str(cell)

        return False


    def isValid(self, cell):
        x_row = cell[0]
        y_col = cell[1]
        if x_row >= 0 and y_col >= 0 and x_row < self.row_nums and y_col < self.col_nums:
            return True
        return False


    def isAtDest(self, cell, area):
        x_row = cell[0]
        y_col = cell[1]
        if area[x_row][y_col] == 9:
            return True
        return False

    def isPath(self, cell, area):
        x_row = cell[0]
        y_col = cell[1]
        if area[x_row][y_col] == 1:
            return True
        return False

    def minimumDistanceBFS(self, numRows, numColumns, area):
        self.row_nums = numRows
        self.col_nums = numColumns

        # each cell has node id - unique of row, col
        # insert each cell in queue

        # Mark all the vertices as not visited
        self.visited = [False] * (len(self.area))
        # Create a queue for BFS
        queue = defaultdict(list)

        s_col = 0
        s_row = 0
        # add current location
        queue[s_row].append(s_col)

        row = 0
        result = -1

        while row < numRows:
            print 'row - ' + str(row)
            col = 0
            while col < numColumns:
                print 'col - ' + str(col)
                result = self.countPaths(area, row, col, paths)
                col += 1
            row += 1

        return result

fd = FindPath()

area = [[1,0,0],
        [1,0,0],
        [1,9,1]]
# print fd.minimumDistanceDFS(3, 3, area)

area = [[1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 9, 0, 0, 0],
        ]

print fd.minimumDistanceDFS(5, 7, area)


def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    i = 1
    newStates = []
    while (days > 0):
        l = size = len(states)
        j = 0

        while size > 0:
            current = states[j]
            if j == 0:
                prev = 0
                next = states[j + 1]
            elif j == (l - 1):
                prev = states[j - 1]
                next = 0
            else:
                next = states[j + 1]
                prev = states[j - 1]

            if next == prev:
                new_state = 0
            else:
                new_state = 1

            states[j] = new_state

            j += 1
            size -= 1

        k = 0
        while k < len(states):
            newStates[k] = states[k]
            k += 1

        i += 1
        days -= 1

    return newStates



# # Driver Code
# l = [4, 8, 16]
#
# num1 = l[0]
# num2 = l[1]
# gcd = find_gcd(num1, num2)
#
# for i in range(5, len(l)):
#     gcd = find_gcd(gcd, l[i])
#
# print(gcd)
#
# num = 5
# arr = [4,8,10]
#
# gcd = generalizedGCD(num, arr)
# print gcd
