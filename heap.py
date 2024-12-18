"""
Custom Heap Implementation for Treasure Management System

This module provides a flexible heap data structure that can be 
customized with different comparison functions.
"""

class Heap:
    def __init__(self, comparison_function, init_array):
        """
        Initialize a heap with a custom comparison function.

        Args:
            comparison_function (callable): Function to determine heap order
            init_array (list): Initial elements to insert into the heap
        """
        self.comparison_function = comparison_function
        self.heap = []
        for elem in init_array:
            self.insert(elem)
    
    def insert(self, value):
        """
        Insert a new value into the heap while maintaining heap property.

        Args:
            value (Any): Value to be inserted
        
        Time Complexity: O(log n)
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def extract(self):
        """
        Remove and return the top element from the heap.

        Returns:
            Any: Top element of the heap

        Raises:
            IndexError: If heap is empty
        
        Time Complexity: O(log n)
        """
        if not self.heap:
            raise IndexError("Extract from an empty heap")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        top_elem = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return top_elem
    
    def top(self):
        """
        Return the top element of the heap without removing it.

        Returns:
            Any: Top element of the heap, or None if heap is empty
        
        Time Complexity: O(1)
        """
        return self.heap[0] if self.heap else None
    
    def _heapify_up(self, index):
        """
        Restore heap property by moving an element up the heap.

        Args:
            index (int): Starting index for heapify_up operation
        """
        parent_index = (index - 1) // 2
        
        while index > 0 and self.comparison_function(self.heap[index], self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        """
        Restore heap property by moving an element down the heap.

        Args:
            index (int): Starting index for heapify_down operation
        """
        n = len(self.heap)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index
            
            if left_child < n and self.comparison_function(self.heap[left_child], self.heap[smallest]):
                smallest = left_child
            
            if right_child < n and self.comparison_function(self.heap[right_child], self.heap[smallest]):
                smallest = right_child
            
            if smallest == index:
                break
        
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
