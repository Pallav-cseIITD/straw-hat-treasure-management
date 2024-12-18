"""
StrawHat Treasury Management System

This module manages treasure processing across multiple crewmates.
"""

import crewmate
import heap
import treasure

def min_load_comparator(x, y):
    """
    Comparator to determine least loaded crewmate.

    Args:
        x, y (CrewMate): Two crewmates to compare

    Returns:
        bool: True if x has less load than y
    """
    return x.complete < y.complete

class StrawHatTreasury:
    def __init__(self, m):
        """
        Initialize StrawHat Treasury with specified number of crewmates.

        Args:
            m (int): Number of crewmates
        """
        self.m = m
        self.rough = []
        self.crewmates_heap = heap.Heap(min_load_comparator, []) 
        self.all_treasures = []

        # Create crewmates
        for _ in range(m):
            cm = crewmate.CrewMate()
            self.crewmates_heap.insert(cm)
            
    def add_treasure(self, treasure):
        """
        Add a treasure to the treasury and assign to least loaded crewmate.

        Args:
            treasure (Treasure): Treasure to be added
        """
        self.all_treasures.append(treasure)
        least_loaded_crewmate = self.crewmates_heap.top()
        
        if len(least_loaded_crewmate.all_crewmate_treasures) == 0:
            self.rough.append(least_loaded_crewmate)
        
        least_loaded_crewmate.add_treasure_crewmate(treasure) 
        self.crewmates_heap.heapify_down(0)
    
    def get_completion_time(self):
        """
        Process all treasures and return sorted list of treasures.

        Returns:
            list: Treasures sorted by ID with completion times
        """
        ans = []
        
        # Process treasures for each crewmate
        for crew in self.rough:
            crew.process_treasure()    
        
        for temp in self.all_treasures:
            ans.append(temp)
        
        # Sort treasures by ID
        return sorted(ans, key=lambda x: x.id)
