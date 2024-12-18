# straw-hat-treasure-management
# Straw Hat Pirates Treasure Management System

## Project Overview
This project simulates a treasure management system for the Straw Hat Pirates, implementing an efficient scheduling algorithm for processing treasures across multiple crewmates.

## Problem Statement
The Straw Hat pirates have collected numerous treasures during their journey. The challenge is to manage these treasures efficiently by:
- Assigning treasures to crewmates with the least current load
- Processing treasures based on specific priority rules
- Tracking completion times for each treasure

## Key Components
- `Treasure`: Represents individual treasure pieces
- `CrewMate`: Manages treasure processing for a single crewmate
- `Heap`: Custom heap implementation for efficient scheduling
- `StrawHatTreasury`: Coordinates treasure assignment and processing

## Scheduling Policy
1. **Treasure Assignment**: 
   - Newly arrived treasure is assigned to the crewmate with the least current load
   - In case of tie, any crewmate can be chosen

2. **Treasure Processing Priority**:
   - Priority = (Wait Time - Remaining Size)
   - In case of equal priority, treasure with the lowest ID is processed first

## Time Complexity
- Treasure Assignment: O(log m + log n)
- Treasure Processing: O(n(log m + log n))

## Usage
```python
# Create treasury with 3 crewmates
treasury = StrawHatTreasury(3)

# Add treasures
treasury.add_treasure(Treasure(1, 5, 0))
treasury.add_treasure(Treasure(2, 3, 2))

# Get completion times
completed_treasures = treasury.get_completion_time()
