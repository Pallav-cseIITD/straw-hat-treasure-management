"""
CrewMate Class for Treasure Management System

This module defines the CrewMate class responsible for processing treasures.
"""

from heap import Heap

def min_priority_comparator(x, y):
    """
    Comparator function to determine treasure processing priority.

    Args:
        x, y (Treasure): Two treasures to compare

    Returns:
        bool: True if x has lower priority than y
    """
    prio_x = x.__dict__.get('remaining_size', 0) + x.arrival_time
    prio_y = y.__dict__.get('remaining_size', 0) + y.arrival_time
    
    if prio_x == prio_y:
        return x.id < y.id
    return prio_x < prio_y

class CrewMate:
    def __init__(self):
        """
        Initialize a CrewMate with empty treasure list and heap.
        """
        self.all_crewmate_treasures = []
        self.treasures_heap = Heap(min_priority_comparator, [])  
        self.complete = 0
    
    def add_treasure_crewmate(self, treasure):
        """
        Add a treasure to the crewmate's list and update completion time.

        Args:
            treasure (Treasure): Treasure to be added
        """
        self.all_crewmate_treasures.append(treasure)
        self.complete = max(self.complete, treasure.arrival_time) + treasure.size

    def process_treasure(self):
        """
        Process all treasures assigned to this crewmate.
        """
        time = 0

        # Initialize remaining size for each treasure
        for tres in self.all_crewmate_treasures:
            tres.__dict__['remaining_size'] = tres.size

        # Process treasures
        for i in range(len(self.all_crewmate_treasures)):
            curr_tres = self.all_crewmate_treasures[i]
            
            # Determine next treasure or finalize processing
            if i+1 < len(self.all_crewmate_treasures):
                next_tres = self.all_crewmate_treasures[i+1]
            else:
                time = curr_tres.arrival_time
                self.treasures_heap.insert(curr_tres)
                
                # Process remaining treasures in heap
                while self.treasures_heap.heap:
                    work_tres = self.treasures_heap.extract()
                    time += work_tres.__dict__['remaining_size']
                    work_tres.completion_time = time
                return

            time = curr_tres.arrival_time
            self.treasures_heap.insert(curr_tres)

            # Process treasures until next treasure's arrival
            while time != next_tres.arrival_time:
                work_tres = self.treasures_heap.top()
                
                if work_tres is None:
                    break

                if time + work_tres.__dict__['remaining_size'] < next_tres.arrival_time:
                    work_tres = self.treasures_heap.extract()
                    time += work_tres.__dict__['remaining_size']
                    work_tres.completion_time = time
                else:
                    work_tres.get_remaining_size(next_tres.arrival_time - time)
                    self.treasures_heap.heapify_down(0)
                    time = next_tres.arrival_time
