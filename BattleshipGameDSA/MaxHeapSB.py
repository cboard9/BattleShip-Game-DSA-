from ScoreNode import *

class MaxHeapSB:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def swap(self, parent_index, child_index):
        parent = self.arr[parent_index]
        child = self.arr[child_index]
        self.arr[child_index] = parent
        self.arr[parent_index] = child

    def heapify_up(self, index):
        parent_index = self.get_parent_index(index)

        while parent_index >= 0:
            left_index = self.get_left_child_index(parent_index)
            right_index = self.get_right_child_index(parent_index)

            parent_score = self.arr[parent_index].score

            left_score = -1
            if self.arr[left_index] is not None:
                left_score = self.arr[left_index].score

            right_score = -1
            if self.arr[right_index] is not None:
                right_score = self.arr[right_index].score

            if left_score >= right_score and left_score > parent_score:
                self.swap(parent_index, left_index)
                parent_index = self.get_parent_index(parent_index)
            elif right_score > parent_score:
                self.swap(parent_index, right_index)
                parent_index = self.get_parent_index(parent_index)
            else:
                break

    def heapify_down(self, parent_index):

        while parent_index < self.size-1:
            left_index = self.get_left_child_index(parent_index)
            right_index = self.get_right_child_index(parent_index)

            parent_score = self.arr[parent_index].score

            left_score = -1
            if self.arr[left_index] is not None:
                left_score = self.arr[left_index].score

            right_score = -1
            if self.arr[right_index] is not None:
                right_score = self.arr[right_index].score

            if left_score >= right_score and left_score > parent_score:
                self.swap(parent_index, left_index)
                parent_index = left_index
            elif right_score > parent_score:
                self.swap(parent_index, right_index)
                parent_index = right_index
            else:
                break

    def insert(self, node):
        value = node.score
        if self.size < self.capacity:
            self.arr[self.size] = node
            self.size += 1
            self.heapify_up(self.size - 1)

    def delete(self):
        first = self.arr[0]
        last = self.arr[self.size - 1]
        self.arr[0] = last
        self.size -= 1
        self.arr[self.size] = None

        self.heapify_down(0)

        return first

    def peek(self):
        return self.arr[0]

