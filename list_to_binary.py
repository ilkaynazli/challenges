"""
    Given a sorted list of integers build a binary search tree of minimal height
    lst = [0, 1, 2, 3, 4, 5, 6]

    tree =          3
                   / \
                  1   5
                 / \ / \
                0  2 4  6
"""
class Node:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right



def list_to_binary(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return Node(nums[0])

    root_index = len(nums)//2
    root = Node(nums[root_index])
 
    left_nums = nums[:root_index]
    right_nums = nums[root_index+1:]

    root.left = Node(list_to_binary(left_nums))
    root.right = Node(list_to_binary(right_nums))

    return root

