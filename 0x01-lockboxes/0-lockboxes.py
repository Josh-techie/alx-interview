#!/usr/bin/python3

def canUnlockAll(boxes):
    # Determines if all the boxes can be opened.
    # :param boxes: List of lists representing locked boxes.
    # :return: True if all boxes can be opened, else False.
    if not boxes:
        return False  # No boxes to open
    # Initialize a set to track reachable boxes
    reachable_boxes = {0}
    # Iterate until no more changes in reachable boxes
    while True:
        # Keep track of the previous set of reachable boxes
        prev_reachable_boxes = set(reachable_boxes)
        # Iterate through keys in all reachable boxes
        for box_id in prev_reachable_boxes.copy():
            # copy for iteration
            reachable_boxes.update(boxes[box_id])
        # Check for changes in reachable boxes
        if prev_reachable_boxes == reachable_boxes:
            break
    # Check if all boxes are reachable
    return len(reachable_boxes) == len(boxes)
