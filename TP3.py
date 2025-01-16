def construct_adj_matrix(edges, num_of_nodes):
    """
    Constructs an adjacency matrix for a directed graph.

    Args:
        edges (list of tuple): List of edges where each edge is represented as a tuple (u, v).
        num_of_nodes (int): Number of nodes in the graph.

    Returns:
        list of list: Adjacency matrix of the graph.
    """
    # Initialize adjacency matrix with zeros
    adj_matrix = [[0] * num_of_nodes for _ in range(num_of_nodes)]

    # Fill the adjacency matrix based on edges
    for u, v in edges:
        if 1 <= u <= num_of_nodes and 1 <= v <= num_of_nodes:
            adj_matrix[u - 1][v - 1] = 1  # Directed graph
        else:
            print(f"Invalid edge: ({u}, {v})")

    return adj_matrix


def print_adj_matrix(matrix):
    """
    Prints the adjacency matrix in a readable format.

    Args:
        matrix (list of list): The adjacency matrix to print.
    """
    for row in matrix:
        print(row)


class TreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def inorder_traversal(root):
    """
    Performs an inorder traversal on a binary tree.

    Args:
        root (TreeNode): The root of the binary tree.
    """
    if root is None:
        return

    # Traverse the left subtree
    inorder_traversal(root.left)

    # Visit the current node
    print(root.label, end=" ")

    # Traverse the right subtree
    inorder_traversal(root.right)


def find_subtree(root, x):
    """
    Finds the subtree rooted at the node with label x.

    Args:
        root (TreeNode): The root of the binary tree.
        x (int): The label of the node to find.

    Returns:
        TreeNode: The subtree rooted at the node with label x, or None if not found.
    """
    if root is None:
        return None

    if root.label == x:
        return root

    # Search in the left and right subtrees
    left_result = find_subtree(root.left, x)
    if left_result:
        return left_result

    return find_subtree(root.right, x)


if __name__ == "__main__":
    # Part (a): Construct adjacency matrix for a graph
    edges = [
        (1, 2), (1, 3), (2, 5), (2, 6),
        (3, 4), (4, 8), (5, 7)
    ]
    num_nodes = 8

    print("a) Construct Adjacent Matrix for graph G:")
    adjacency_matrix = construct_adj_matrix(edges, num_nodes)
    print_adj_matrix(adjacency_matrix)

    # Part (b): Perform inorder traversal on a subtree
    print("\nb) Inorder Algorithm:")

    # Build the binary tree
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)

    root.right = TreeNode(2)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(7)

    # Input for subtree root label
    x = int(input("Enter the root label of the subtree to traverse (inorder): "))

    # Find the subtree and perform inorder traversal
    subtree_root = find_subtree(root, x)
    if subtree_root:
        print(f"Inorder traversal of subtree rooted at node {x}:")
        inorder_traversal(subtree_root)
    else:
        print(f"Node {x} not found in the tree.")
