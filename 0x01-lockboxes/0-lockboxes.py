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
    # Initialize a set to track opened boxes
    opened_boxes = set()
    opened_boxes.add(0)  # Start with the first box
    # Initialize a queue for BFS
    queue = [0]
    while queue:
        current_box = queue.pop(0)  # Get the front of the queue
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)  # Mark the box as opened
                queue.append(key)  # Add key to the queue for further explo
    return len(opened_boxes) == len(boxes)
