"""
Treasure Class for Straw Hat Pirates Treasure Management System

This module defines the Treasure class used in the treasure management simulation.
Each treasure has unique attributes like ID, size, and arrival time.
"""

class Treasure:
    def __init__(self, id, size, arrival_time):
        """
        Initialize a Treasure object with its unique characteristics.

        Args:
            id (int): Unique identifier for the treasure
            size (int): Time units required to process the treasure
            arrival_time (int): Time when the treasure becomes available for processing
        """
        self.id = id
        self.size = size
        self.arrival_time = arrival_time
        self.completion_time = None  # Will be set during processing
    
    def get_remaining_size(self, unit=0):
        """
        Update the processed size of the treasure.
        
        Args:
            unit (int): Time units processed, defaults to 0
        """
        if 'remaining_size' not in self.__dict__:
            self.__dict__['remaining_size'] = self.size  # Initialize if not present
        self.__dict__['remaining_size'] -= unit
