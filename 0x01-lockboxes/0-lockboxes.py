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
    """ Method that determines if all boxes can be opened """

    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False
    return True
