# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # Convert to_delete list to a set for O(1) lookups
        to_delete_set = set(to_delete)
        # List to store the roots of the resulting forest
        forest = []
        
        def dfs(node, is_root):
            if not node:
                return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            # Recursively process the left and right children
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            return None if root_deleted else node
        
        # Start DFS traversal from the root
        dfs(root, True)
        return forest
