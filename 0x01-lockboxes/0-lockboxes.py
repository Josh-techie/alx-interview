#!/usr/bin/python3

# def canUnlockAll(boxes):
#     # suppose box 0 is unlocked
#     unlocked = [0]
#     # take index of the box iterate and compare it with the key of the list
#     #  in the big list
#     for box_id, box in enumerate(boxes):
#         if not box:
#             continue
#         for key in box:
#             # if matched continue iteration else return false
#             if key < len(boxes) and key not in unlocked and key != box_id:
#                 unlocked.append(key)
#     if len(unlocked) == len(boxes):
#         return True
#     return False

def canUnlockAll(boxes):
    if not boxes:
        return False  # No boxes to open
    # Initialize a set to track reachable boxes
    reachable_boxes = {0}
    # Iterate until no more changes in reachable boxes
    while True:
        # Keep track of the previous set of reachable boxes
        prev_reachable_boxes = set(reachable_boxes)
        # Iterate through keys in all reachable boxes
        for box_id in prev_reachable_boxes.copy():  # copy for iteration
            reachable_boxes.update(boxes[box_id])
        # Check for changes in reachable boxes
        if prev_reachable_boxes == reachable_boxes:
            break
    # Check if all boxes are reachable
    return len(reachable_boxes) == len(boxes)
